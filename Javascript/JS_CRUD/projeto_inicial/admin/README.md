# How to start the JSON server

1. Open the admin folder in vscode and run the command:

```console
json-server --watch db.json
```

2. You will need to use a server simulator like browser-sync or live-server.

    - **[Browser-sync](https://browsersync.io/)**:

        ```console
        browser-sync start --server --file . --host --port 5000 --startPath admin/telas/lista_cliente.html
        ```

    - **[Live-server (vscode plugin)](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)**:

       You will only need to start it.
