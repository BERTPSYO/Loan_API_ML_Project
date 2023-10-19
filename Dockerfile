From python:3.10-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile","Pipfile.lock","./"]

RUN pipenv install --deploy --system


COPY ["./src/predictionModel1/model_Pred_1.bin", "./src/predictionModel1/ModelPred.py", "./src/predictionModel1/"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "src.predictionModel1.ModelPred:app"]