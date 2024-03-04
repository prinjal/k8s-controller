from kubernetes import client, config, watch

def main():
    config.load_kube_config()
    v1 = client.CoreV1Api()

    w = watch.Watch()
    for event in w.stream(v1.list_pod_for_all_namespaces):
        print("Hello")
        print(f"Event: {event['type']} Pod: {event['object'].metadata.name}")

if __name__ == '__main__':
    main()
