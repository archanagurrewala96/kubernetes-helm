#Kubernetes: Creation of multiple deployments with single deployment file using Helm

####NOTE: I use Helm charts in this Project. To know more about what Helm is can refer to my medium article https://medium.com/@archana.gurrewala96/introduction-to-helm-207657ad3e7f 
####Let's say we have usecase wherein we need multiple pods which does same functionality but differs in some variables for each pod. In that case we can declare those variables in values.yaml file and loop those variables in deployment.yaml file.


We can give the variables which differ for each pod in values.yaml as below
```buildoutcfg
details:
  - podname: pod1
    username: user1
  - podname: pod2
    username: user2
```

Now we can call these variables from templates/deployment.yaml file in a loop as below
```buildoutcfg
{{- range $details := .Values.details }}
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ $details.podname}}
  name: {{ $details.podname}}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ $details.podname}}
  template:
    metadata:
      labels:
        app: {{ $details.podname}}
    spec:
      containers:
      - image: gcr.io/archana-test/sample:13
        name: {{ $details.podname}}
        env:
          - name: Username
            value: {{ $details.username}}
---
{{- end }}

```