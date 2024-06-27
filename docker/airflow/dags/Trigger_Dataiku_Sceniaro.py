import sys
import dataikuapi
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import PythonOperator

def Trigger_Dataiku():
    scenario_name = 'ETL_DEMO'
    host = 'http://dataiku:10000'  
    api_key = 'hpmH8GJyEfCkpkBbOWU5RV4WMWmZ3V5K'
    project_key = 'DWH_SNOWFLAKE'
    client = dataikuapi.DSSClient(host, api_key)
    client._session.verify = False
    print('Connected Successfully!')

    # Get the project by its key
    project = client.get_project(project_key)

    # Get the required scenario to run the flow in Dataiku project
    scenario = project.get_scenario(scenario_name)

    # Trigger the scenario on this project 
    try:
        trigger = scenario.run_and_wait()
        if trigger.outcome == "SUCCESS":
            print("<=>"*20, "Dataiku Job Completed")
        else:
            print("<=>"*20, "Dataiku Job Failed", trigger.get_info())
    except dataikuapi.utils.DataikuException as e:
        print(f"Failed to run the scenario: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

default_args = {
    'owner': 'DuckyBonbon',
    'depends_on_past': False,
    'start_date': datetime(2024, 6, 26),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag_params = {
    'dag_id' : 'Dataiku_Trigger_Example',
    'default_args' : default_args,
    'schedule_interval' : "0 8 * * *" # Run every day at 8am
}

with DAG(**dag_params, catchup=False) as dag:

    start = DummyOperator(task_id='start', dag=dag)

    trigger_dataiku_job = PythonOperator(
        task_id = 'Trigger_Dataiku_Sceniaro',
        python_callable = Trigger_Dataiku
    )

    end = DummyOperator(task_id='end', dag=dag)

    start >> trigger_dataiku_job >> end