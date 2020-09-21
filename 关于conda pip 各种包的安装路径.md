## 问题
前几天碰到了一些头疼的问题，主要是python包安装太乱，之前装conda之前就装了好几个版本的python，23都有，环境变量也填的乱七八糟。jupyter notebook突然就连不上kernel，现实的错误是
``` 
[E 01:46:30.552 NotebookApp] 500 POST /api/sessions (::1) 3719.90ms referer=http://localhost:8888/notebooks/Downloads/FIR-01.ipynb
[W 01:51:30.469 NotebookApp] Notebook Downloads/FIR-01.ipynb is not trusted
[E 01:51:32.922 NotebookApp] Uncaught exception POST /api/sessions (::1)
    HTTPServerRequest(protocol='http', host='localhost:8888', method='POST', uri='/api/sessions', version='HTTP/1.1', remote_ip='::1')
    Traceback (most recent call last):
      File "C:\Users\lenovo\AppData\Roaming\Python\Python37\site-packages\tornado\web.py", line 1703, in _execute
        result = await result
      File "C:\Users\lenovo\AppData\Roaming\Python\Python37\site-packages\tornado\gen.py", line 742, in run
        yielded = self.gen.throw(*exc_info)  # type: ignore
      File "C:\Users\lenovo\AppData\Roaming\Python\Python37\site-packages\notebook\services\sessions\handlers.py", line 72, in post
        type=mtype))
      File "C:\Users\lenovo\AppData\Roaming\Python\Python37\site-packages\tornado\gen.py", line 735, in run
        value = future.result()
      File "C:\Users\lenovo\AppData\Roaming\Python\Python37\site-packages\tornado\gen.py", line 742, in run
        yielded = self.gen.throw(*exc_info)  # type: ignore
      File "C:\Users\lenovo\AppData\Roaming\Python\Python37\site-packages\notebook\services\sessions\sessionmanager.py", line 88, in create_session
        kernel_id = yield self.start_kernel_for_session(session_id, path, name, type, kernel_name)
      File "C:\Users\lenovo\AppData\Roaming\Python\Python37\site-packages\tornado\gen.py", line 735, in run
        value = future.result()
      File "C:\Users\lenovo\AppData\Roaming\Python\Python37\site-packages\tornado\gen.py", line 742, in run
        yielded = self.gen.throw(*exc_info)  # type: ignore
      File "C:\Users\lenovo\AppData\Roaming\Python\Python37\site-packages\notebook\services\sessions\sessionmanager.py", line 101, in start_kernel_for_session
        self.kernel_manager.start_kernel(path=kernel_path, kernel_name=kernel_name)
      File "C:\Users\lenovo\AppData\Roaming\Python\Python37\site-packages\tornado\gen.py", line 735, in run
        value = future.result()
      File "C:\Users\lenovo\AppData\Roaming\Python\Python37\site-packages\notebook\services\kernels\kernelmanager.py", line 176, in start_kernel
        kernel_id = await maybe_future(self.pinned_superclass.start_kernel(self, **kwargs))
      File "C:\Users\lenovo\AppData\Roaming\Python\Python37\site-packages\jupyter_client\multikernelmanager.py", line 185, in start_kernel
        km.start_kernel(**kwargs)
      File "C:\Users\lenovo\AppData\Roaming\Python\Python37\site-packages\jupyter_client\manager.py", line 309, in start_kernel
        kernel_cmd, kw = self.pre_start_kernel(**kw)
      File "C:\Users\lenovo\AppData\Roaming\Python\Python37\site-packages\jupyter_client\manager.py", line 256, in pre_start_kernel
        self.write_connection_file()
      File "C:\Users\lenovo\AppData\Roaming\Python\Python37\site-packages\jupyter_client\connect.py", line 474, in write_connection_file
        kernel_name=self.kernel_name
      File "C:\Users\lenovo\AppData\Roaming\Python\Python37\site-packages\jupyter_client\connect.py", line 138, in write_connection_file
        with secure_write(fname) as f:
      File "d:\anaconda3\lib\contextlib.py", line 112, in __enter__
        return next(self.gen)
      File "C:\Users\lenovo\AppData\Roaming\Python\Python37\site-packages\jupyter_core\paths.py", line 435, in secure_write
        win32_restrict_file_to_user(fname)
      File "C:\Users\lenovo\AppData\Roaming\Python\Python37\site-packages\jupyter_core\paths.py", line 361, in win32_restrict_file_to_user
        import win32api
    ImportError: DLL load failed: %1 不是有效的 Win32 应用程序。
```
 发现是python包和版本的位数不符合，有的让重装piwin32，说实话全都是治标不治本，乱七八糟，全部重装了一次也没啥用，还是应该好好深入了解一下问题根本。
基本就能确定是安装路径和环境变量的问题，一会儿从D盘读 一会儿用C盘的Lenovo/roaming，还是乱七八糟，借此机会清理一下
### conda介绍
#### 包管理的原理
#### 关于pip
#### 下载路径
### 环境变量的设置
