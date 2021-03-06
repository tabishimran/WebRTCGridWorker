class MSG_FIELD:
    TYPE = "type"
    FROM = "from"
    DESTINATION = "destination"
    CONTENT = "content"
    NODE_ID = "node_id"
    PAYLOAD = "payload"
    NODES = "nodes"
    MODELS = "models"
    DATASETS = "datasets"
    CPU = "cpu"
    MEM_USAGE = "mem_usage"


class GRID_EVENTS:
    JOIN = "join"
    FORWARD = "grid-forward"
    FORWARD = "forward"
    MONITOR_ANSWER = "monitor-answer"


class NODE_EVENTS:
    MONITOR = "monitor"
    WEBRTC_SCOPE = "create-webrtc-scope"
    WEBRTC_OFFER = "webrtc-offer"
    WEBRTC_ANSWER = "webrtc-answer"
