# readme-handler

To generate a readme into the html make following stept:

```shell
$ cd dashboard
$ npm install

$ npm run build


$ cd ../batch
$ python3 datahandler.py
```

`datahandler.py` will create htmls into the `batch/export` folder from the dashboard dist.
