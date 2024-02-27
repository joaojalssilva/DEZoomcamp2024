export SPARK_HOME="/workspaces/DEZoomcamp2024/spark-3.5.1-bin-hadoop3"
export PATH="/workspaces/DEZoomcamp2024/spark-3.5.1-bin-hadoop3/bin:${PATH}"


export PYTHONPATH="${SPARK_HOME}/python/:$PYTHONPATH"
export PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.9-src.zip:$PYTHONPATH"


http://localhost:4040/jobs/