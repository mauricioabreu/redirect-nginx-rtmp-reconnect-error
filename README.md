# NGINX-RTMP demo for issue sergey-dryabzhinsky/nginx-rtmp-module 310

## How to run

Start the ingest server (NGINX-RTMP to redirect streaming):
```
make start_ingest            
```


Start the ingest server (NGINX-RTMP to save HLS data):
```
make start_segmenter
```

Start the auth app:
```
make start_auth
```

Ingest some video:
```
make ingest_colors 
```