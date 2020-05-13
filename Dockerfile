FROM python:3.7
ARG VERSION=1.0.0
LABEL com.HotspotHousing.version=$VERSION
ENV PYTHONUNBUFFERED 1
ENV STATUS="Development"

WORKDIR usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8080"]
