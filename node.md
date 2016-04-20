# CORS
python manage时候，django-cors-headers会出现问题:No module named corsheaders,因其没有model?

测试跨域

```js
a=$.get("http://192.168.99.101:8000/snippets/snappets/1")
$.parseJSON(a.responseText).code
```
