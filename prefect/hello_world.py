
from datasets import list_datasets, load_dataset, list_metrics, load_metric
import prefect
from prefect import task, Flow, Parameter
from prefect.triggers import manual_only
from prefect.engine.executors import LocalDaskExecutor

@task
def first_task(x):
    print("Printing First task name: " + x)

@task
def second_task(x):
    print("Printing the second task:" + x)

@task
def third_task(x):
    print("Printing the third task:" + x)

def prefect_flow():

    with Flow("SeqFlow") as flow:

        first_task("no_1")
        second_task("no_2")
        third_task("no_3")
    return flow


if __name__=='__main__':
    flow = prefect_flow()
    flow.run()

