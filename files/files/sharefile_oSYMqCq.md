# Share Story

## Langkah - langkah
1. Buat project baru dengan nama `share_story`
2. Buat app baru dengan nama `main`
2. Buat routing sesuai dengan table berikut

|Project URL|App|App URL|Views|URL name|Template|
|---|---|---|---|---|---|
|`' '` |main|`' '`|`views.index`|`index`|`main/index.html`|
||main|`'story/create/'`|`views.create`|`create`||
||main|`'story/update/<int:story_id>'`|`views.update`|`update`||
||main|`'story/delete/<int:story_id>'`|`views.delete`|`delete`||

4. Buat model baru dengan nama `Story` dengan deskripsi sebagai berikut

![main/models.py](https://kod.so/gen?code=class+Story%28models.Model%29%3A%0A++++nickname+%3D+models.CharField%28max_length%3D10%29%0A++++password+%3D+models.TextField%28%29%0A++++story+%3D+models.CharField%28max_length%3D140%29++++%0A++++created_at+%3D+models.DateTimeField%28auto_now_add%3DTrue%29%0A++++updated_at+%3D+models.DateTimeField%28auto_now%3DTrue%29&num=1&lang=python&title=%2Fmain%2Fmodels.py&watermark=&background=none&theme=monokai&codeFontName=hack&tabSize=4&shadow=0&paddingtb=3&paddinglr=3)

5. Buat 3 buah file html dan simpan di dalam `templates/main`
	- base.html
	- index.html
	- edit_story.html

6. Siapkan folder static di sini
![siapkan folder static](/home/mxme/Downloads/kod%20(3).png)