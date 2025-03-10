## sys
`sys 模块提供了一系列用于与 Python 解释器和它的环境进行交互的函数和变量。`

sys 模块常用的函数和变量有：

- `sys.argv`：命令行参数列表。
- `sys.exit(status=0)`：退出程序，并返回一个状态码。
- `sys.version`：Python 解释器的版本信息。
- `sys.platform`：操作系统平台名称。
- `sys.path`：模块的搜索路径。
- `sys.modules`：已导入的模块的字典。
- `sys.stdin`：标准输入流。
- `sys.stdout`：标准输出流。
- `sys.stderr`：标准错误流。
- `sys.getrefcount(object)`：返回对象的引用计数。
- `sys.setrecursionlimit(limit)`：设置递归的最大深度。


## os
`os 模块提供了一系列用于处理文件和目录的函数和变量。`

os 模块常用的函数和变量有：

- `os.name`：操作系统类型。
- `os.path.join(path, *paths)`：将多个路径组合成一个路径。
- `os.path.split(path)`：将路径分割成目录和文件名。
- `os.path.splitext(path)`：将路径分割成文件名和扩展名。
- `os.path.exists(path)`：判断路径是否存在。
- `os.path.isfile(path)`：判断路径是否为文件。
- `os.path.isdir(path)`：判断路径是否为目录。
- `os.path.getsize(path)`：获取文件大小。
- `os.path.getmtime(path)`：获取文件最后修改时间。
- `os.path.getatime(path)`：获取文件最后访问时间。
- `os.path.getctime(path)`：获取文件创建时间。
- `os.listdir(path)`：列出目录下的文件和目录。
- `os.mkdir(path)`：创建目录。
- `os.makedirs(path)`：递归创建目录。
- `os.remove(path)`：删除文件。
- `os.removedirs(path)`：递归删除目录。
- `os.rename(src, dst)`：重命名文件或目录。
- `os.stat(path)`：获取文件或目录的状态信息。
- `os.chmod(path, mode)`：修改文件或目录的权限。
- `os.utime(path, times)`：修改文件或目录的最后访问和修改时间。
- `os.walk(top)`：遍历目录树。
- `os.getenv(key, default=None)`：获取环境变量的值。
- `os.putenv(key, value)`：设置环境变量的值。
- `os.unsetenv(key)`：删除环境变量。

## shutil
`shutil 模块提供了一系列用于高级文件操作的函数。`

shutil 模块常用的函数和变量有：

- `shutil.copyfile(src, dst)`：复制文件。
- `shutil.copymode(src, dst)`：复制文件权限。
- `shutil.copystat(src, dst)`：复制文件状态。
- `shutil.copy(src, dst)`：复制文件或目录。
- `shutil.copy2(src, dst)`：复制文件或目录，同时复制元数据。
- `shutil.copytree(src, dst, symlinks=False, ignore=None)`：递归复制目录。
- `shutil.rmtree(path)`：递归删除目录。
- `shutil.move(src, dst)`：移动文件或目录。
- `shutil.disk_usage(path)`：获取磁盘使用情况。
- `shutil.chown(path, user=None, group=None)`：修改文件或目录的用户和组。
- `shutil.which(cmd)`：查找命令的路径。

## datetime
`datetime 模块提供了日期和时间处理的类。`

datetime 模块常用的类和方法有：

- `datetime.datetime.now()`：获取当前日期和时间。
- `datetime.datetime.utcnow()`：获取当前日期和时间（UTC 时间）。
- `datetime.datetime.fromtimestamp(timestamp)`：根据时间戳获取日期和时间。
- `datetime.datetime.strptime(date_string, format)`：根据格式字符串获取日期和时间。
- `datetime.datetime.strftime(datetime_object, format)`：根据格式字符串格式化日期和时间。
- `datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)`：时间差。
- `datetime.date.today()`：获取当前日期。
- `datetime.date.fromtimestamp(timestamp)`：根据时间戳获取日期。
- `datetime.date.fromordinal(ordinal)`：根据序数获取日期。
- `datetime.date.fromisoformat(date_string)`：根据 ISO 格式字符串获取日期。
- `datetime.date.isocalendar(year, week, day)`：获取年份、周数和星期几。
- `datetime.date.weekday(date_object)`：获取星期几。
- `datetime.date.isoweekday(date_object)`：获取星期几（ISO 格式）。
- `datetime.date.isleap(year)`：判断是否为闰年。
- `datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, fold=0)`：时间。
- `datetime.time.fromisoformat(time_string)`：根据 ISO 格式字符串获取时间。
- `datetime.time.isoformat(time_object)`：根据时间对象获取 ISO 格式字符串。
- `datetime.time.strftime(time_object, format)`：根据格式字符串格式化时间。
- `datetime.timezone(offset, name=None)`：时区。
- `datetime.timedelta.total_seconds(self)`：获取时间差的总秒数。
- `datetime.tzinfo.utcoffset(self, dt)`：获取时区偏移量。
- `datetime.tzinfo.dst(self, dt)`：获取夏令时偏移量。
- `datetime.tzinfo.tzname(self, dt)`：获取时区名称。
- `datetime.tzinfo.fromutc(self, dt)`：根据 UTC 时间获取本地时间。

## random
`random 模块提供了生成随机数的函数。`

random 模块常用的函数有：

- `random.random()`：生成一个随机浮点数。
- `random.uniform(a, b)`：生成一个随机浮点数，范围在 a 和 b 之间。
- `random.randint(a, b)`：生成一个随机整数，范围在 a 和 b 之间。
- `random.randrange(start, stop=None, step=1, int=None)`：生成一个随机整数，范围在 start 和 stop 之间，步长为 step。
- `random.choice(seq)`：从序列中随机选择一个元素。
- `random.sample(population, k)`：从序列中随机选择 k 个不重复的元素。
- `random.shuffle(x)`：将序列 x 随机打乱。
- `random.gauss(mu, sigma)`：生成一个符合高斯分布的随机数。
- `random.betavariate(alpha, beta)`：生成一个符合 Beta 分布的随机数。
- `random.expovariate(lambd)`：生成一个符合指数分布的随机数。
- `random.gammavariate(alpha, beta)`：生成一个符合 Gamma 分布的随机数。

## time
`time 模块提供了时间相关的函数。`

time 模块常用的函数有：

- `time.time()`：获取当前时间戳。
- `time.clock()`：获取 CPU 时间。
- `time.sleep(seconds)`：暂停程序运行。
- `time.ctime(timestamp)`：根据时间戳获取日期和时间。
- `time.gmtime(timestamp)`：根据时间戳获取 UTC 日期和时间。
- `time.localtime(timestamp)`：根据时间戳获取本地日期和时间。
- `time.strftime(format, timestamp)`：根据格式字符串格式化日期和时间。
- `time.strptime(date_string, format)`：根据格式字符串解析日期和时间。
- `time.mktime(time_tuple)`：根据时间元组获取时间戳。
- `time.monotonic()`：获取系统的实时时间。
- `time.perf_counter()`：获取系统的高精度时间。
- `time.process_time()`：获取进程的 CPU 时间。
- `time.thread_time()`：获取线程的 CPU 时间。

## collections
`collections 模块提供了一些有用的集合类。`

collections 模块常用的类有：

- `collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)`：创建命名元组。
- `collections.deque(iterable, maxlen=None)`：创建双端队列。
- `collections.Counter(iterable=None, **kwargs)`：创建计数器。
- `collections.OrderedDict(iterable=None, **kwargs)`：创建有序字典。
- `collections.defaultdict(default_factory=None, **kwargs)`：创建默认字典。
- `collections.UserDict(dict)`：创建用户字典。
- `collections.UserList(list)`：创建用户列表。
- `collections.UserString(string)`：创建用户字符串。

## re
`re 模块提供了正则表达式处理的函数。`

re 模块常用的函数有：

- `re.match(pattern, string, flags=0)`：匹配字符串的开始位置。
- `re.search(pattern, string, flags=0)`：搜索字符串。
- `re.findall(pattern, string, flags=0)`：搜索字符串，返回所有匹配的子串。
- `re.finditer(pattern, string, flags=0)`：搜索字符串，返回一个迭代器，每次迭代返回一个匹配的子串。
- `re.sub(pattern, repl, string, count=0, flags=0)`：替换字符串中的子串。
- `re.subn(pattern, repl, string, count=0, flags=0)`：替换字符串中的子串，并返回替换后的字符串和替换次数。
- `re.split(pattern, string, maxsplit=0, flags=0)`：分割字符串。
- `re.escape(pattern)`：转义正则表达式中的特殊字符。
- `re.purge()`：清除正则表达式缓存。
- `re.compile(pattern, flags=0)`：编译正则表达式。

## argparse
`argparse 模块提供了命令行参数解析的函数。`
 
 argparse 模块常用的函数有：

- `argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True)`：创建解析器。
- `parser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])`：添加命令行参数。
- `parser.parse_args()`：解析命令行参数。
- `parser.print_help()`：打印帮助信息。
- `parser.error(message)`：打印错误信息并退出程序。

## base64
`base64 模块提供了 Base64 编码和解码的函数。`

base64 模块常用的函数有：

- `base64.b64encode(s)`：编码字符串。
- `base64.b64decode(s)`：解码字符串。
- `base64.b64encode(s, altchars=None)`：编码字符串，指定替代字符。
- `base64.b64decode(s, altchars=None, validate=False)`：解码字符串，指定替代字符。
- `base64.urlsafe_b64encode(s)`：编码 URL 安全的字符串。
- `base64.urlsafe_b64decode(s)`：解码 URL 安全的字符串。
- `base64.b32encode(s)`：编码 Base32 字符串。
- `base64.b32decode(s)`：解码 Base32 字符串。
- `base64.b16encode(s)`：编码 Base16 字符串。
- `base64.b16decode(s)`：解码 Base16 字符串。

## struct
`struct 模块提供了打包和解包 C 结构体的函数。`

struct 模块常用的函数有：

- `struct.pack(fmt, v1, v2, ...)`：打包数据。
- `struct.unpack(fmt, buffer)`：解包数据。
- `struct.calcsize(fmt)`：计算格式占用字节数。

## hashlib
`hashlib 模块提供了哈希算法的函数。`

hashlib 模块常用的函数有：

- `hashlib.md5(data)`：计算 MD5 哈希值。
- `hashlib.sha1(data)`：计算 SHA1 哈希值。
- `hashlib.sha224(data)`：计算 SHA224 哈希值。
- `hashlib.sha256(data)`：计算 SHA256 哈希值。
- `hashlib.sha384(data)`：计算 SHA384 哈希值。
- `hashlib.sha512(data)`：计算 SHA512 哈希值。
- `hashlib.new(name, data=b'', **kwargs)`：创建哈希对象。

## hmac
`hmac 模块提供了哈希消息认证码 (HMAC) 的函数。`

 hmac 模块常用的函数有：

- `hmac.new(key, msg=b'', digestmod=None)`：创建 HMAC 对象。
- `hmac.digest(key, msg=b'', digestmod=None)`：计算 HMAC 值。
- `hmac.hexdigest(key, msg=b'', digestmod=None)`：计算 HMAC 值，并以十六进制字符串形式返回。


## itertools
`itertools 模块提供了创建迭代器的函数。`

itertools 模块常用的函数有：

- `itertools.count(start=0, step=1)`：创建一个无限的迭代器，每次迭代返回 start 加上 step 的值。
- `itertools.cycle(iterable)`：创建一个无限的迭代器，每次迭代返回 iterable 中的元素。
- `itertools.repeat(object, times=None)`：创建一个迭代器，重复 object 直到迭代结束。
- `itertools.chain(iterable1, iterable2, ...)`：创建一个迭代器，返回多个迭代器中的元素。
- `itertools.compress(data, selectors)`：创建一个迭代器，返回 selectors 中为 True 的元素。
- `itertools.dropwhile(predicate, iterable)`：创建一个迭代器，从 iterable 中跳过满足 predicate 的元素，返回剩余的元素。
- `itertools.filterfalse(predicate, iterable)`：创建一个迭代器，返回 iterable 中不满足 predicate 的元素。
- `itertools.groupby(iterable, key=None)`：创建一个迭代器，返回按 key 排序的元素。
- `itertools.islice(iterable, start, stop, step)`：创建一个迭代器，返回 iterable 中指定范围的元素。
- `itertools.starmap(function, iterable)`：创建一个迭代器，将 iterable 中每个元素作为参数调用 function。
- `itertools.takewhile(predicate, iterable)`：创建一个迭代器，返回 iterable 中满足 predicate 的元素。
- `itertools.zip_longest(iterable1, iterable2, ...)`：创建一个迭代器，返回多个迭代器中最短的元素。

## functools
`functools 模块提供了高阶函数的函数。`

functools 模块常用的函数有：

- `functools.partial(func, *args, **keywords)`：创建一个偏函数。
- `functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)`：更新函数的属性。
- `functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)`：更新函数的属性。
- `functools.reduce(function, iterable, initializer=None)`：对 iterable 中元素进行累积。
- `functools.lru_cache(maxsize=128, typed=False)`：创建一个缓存函数。
- `functools.singledispatch(func)`：创建一个单分派函数。
- `functools.singledispatchmethod(func)`：创建一个单分派方法。
- `functools.partialmethod(func, *args, **keywords)`：创建一个偏方法。
- `functools.total_ordering(cls)`：为类添加全序关系。

## contextlib
`contextlib 模块提供了上下文管理器的函数。`

contextlib 模块常用的函数有：

- `contextlib.contextmanager(func)`：创建一个上下文管理器。
- `contextlib.closing(thing)`：创建一个上下文管理器，关闭 thing。
- `contextlib.nullcontext(enter_result=None)`：创建一个空的上下文管理器。
- `contextlib.redirect_stdout(new_target)`：创建一个上下文管理器，重定向 stdout。
- `contextlib.redirect_stderr(new_target)`：创建一个上下文管理器，重定向 stderr。
- `contextlib.redirect_stdout(new_target)`：创建一个上下文管理器，重定向 stdout。
- `contextlib.redirect_stderr(new_target)`：创建一个上下文管理器，重定向 stderr。
- `contextlib.suppress(exception)`：创建一个上下文管理器，忽略 exception。
- `contextlib.ContextDecorator(func)`：创建一个上下文装饰器。

## urllib
`urllib 模块提供了 URL 处理的函数。`

urllib 模块常用的函数有：

- `urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)`：解析 URL。
- `urllib.parse.urlunparse(parts)`：拼接 URL。
- `urllib.parse.urljoin(base, url, allow_fragments=True)`：拼接 URL。
- `urllib.parse.urlencode(query, doseq=False, safe='', encoding=None, errors=None)`：编码查询字符串。
- `urllib.parse.parse_qs(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace')`：解析查询字符串。
- `urllib.parse.parse_qsl(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace')`：解析查询字符串。
- `urllib.parse.quote(string, safe='/')`：编码字符串。
- `urllib.parse.quote_plus(string, safe='')`：编码字符串，将空格编码为加号。
- `urllib.parse.unquote(string, encoding='utf-8', errors='replace')`：解码字符串。


## XML
`xml 模块提供了处理 XML 的函数。`

xml 模块常用的函数有：

- `xml.etree.ElementTree.Element(tag, attrib={}, **extra)`：创建元素。
- `xml.etree.ElementTree.SubElement(parent, tag, attrib={}, **extra)`：创建子元素。
- `xml.etree.ElementTree.tostring(element, encoding='unicode', method='xml', *, short_empty_elements=True)`：将元素转换为字符串。
- `xml.etree.ElementTree.parse(source, parser=None, **kwargs)`：解析 XML。
- `xml.etree.ElementTree.iterparse(source, events=None, *, tag=None, encoding='utf-8', strip_cdata=False, remove_blank_text=True, recover=True)`：解析 XML，返回迭代器。
- `xml.etree.ElementTree.fromstring(text, parser=None, **kwargs)`：解析 XML 字符串。
- `xml.etree.ElementTree.XML(text, parser=None, **kwargs)`：解析 XML 字符串。
- `xml.dom.minidom.parse(filename, parser=None)`：解析 XML 文件。
- `xml.dom.minidom.parseString(string, parser=None)`：解析 XML 字符串。
- `xml.dom.minidom.getDOMImplementation()`：获取 DOM 实现。
- `xml.dom.minidom.parse(filename, parser=None)`：解析 XML 文件。
- `xml.dom.minidom.parseString(string, parser=None)`：解析 XML 字符串。
- `xml.dom.minidom.getDOMImplementation()`：获取 DOM 实现。
- `xml.dom.minidom.Node.toxml(encoding='utf-8')`：将节点转换为字符串。


## HTMLParser
`HTMLParser 模块提供了处理 HTML 的函数。`

HTMLParser 模块常用的函数有：

- `HTMLParser.HTMLParser(convert_charrefs=True)`：创建 HTML 解析器。
- `parser.feed(data)`：解析 HTML 字符串。
- `parser.close()`：关闭解析器。
- `parser.getpos()`：获取当前位置。
- `parser.get_starttag_text()`：获取开始标签。
- `parser.get_endtag_text()`：获取结束标签。
- `parser.get_starttag_text()`：获取开始标签。
- `parser.get_endtag_text()`：获取结束标签。
- `parser.handle_starttag(tag, attrs)`：处理开始标签。
- `parser.handle_endtag(tag)`：处理结束标签。
- `parser.handle_startendtag(tag, attrs)`：处理开始结束标签。
- `parser.handle_data(data)`：处理数据。
- `parser.handle_charref(name)`：处理字符引用。
- `parser.handle_entityref(name)`：处理实体引用。
- `parser.handle_decl(decl)`：处理声明。
- `parser.handle_pi(data)`：处理处理指令。
- `parser.handle_comment(data)`：处理注释。
- `parser.handle_decl(decl)`：处理声明。
- `parser.unknown_decl(data)`：处理未知声明。
- `parser.reset()`：重置解析器。
- `parser.reset()`：重置解析器。
- `parser.error(message)`：打印错误信息。
- `parser.get_starttag_text()`：获取开始标签。
- `parser.get_endtag_text()`：获取结束标签。
- `parser.get_starttag_text()`：获取开始标签。
- `parser.get_endtag_text()`：获取结束标签。

## venv
`venv 模块提供了创建虚拟环境的函数。`

venv 模块常用的函数有：

- `venv.create(env_dir, with_pip=True, clear=False)`：创建虚拟环境。
- `venv.EnvBuilder(system_site_packages=False, clear=False, symlinks=False, upgrade=False, with_pip=True)`：创建虚拟环境的构建器。
- `venv.create(env_dir, with_pip=True, clear=False)`：创建虚拟环境。
- `venv.EnvBuilder(system_site_packages=False, clear=False, symlinks=False, upgrade=False, with_pip=True)`：创建虚拟环境的构建器。
- `venv.EnvBuilder.create(env_dir)`：创建虚拟环境。
- `venv.EnvBuilder.clear_directory(path)`：清除目录。

## http
`http 模块提供了 HTTP 客户端的函数。`

http 模块常用的函数有：

- `http.client.HTTPConnection(host, port=None, timeout=None, source_address=None, blocksize=8192, *, source_address=None)`：创建 HTTP 连接。
- `http.client.HTTPSConnection(host, port=None, timeout=None, source_address=None, blocksize=8192, *, context=None, check_hostname=None)`：创建 HTTPS 连接。
- `http.client.HTTPResponse(sock, debuglevel=0, method=None, url=None)`：创建 HTTP 响应。
- `http.client.HTTPConnection.request(method, url, body=None, headers=None)`：发送 HTTP 请求。
- `http.client.HTTPConnection.getresponse()`：获取 HTTP 响应。
- `http.client.HTTPConnection.set_debuglevel(level)`：设置调试级别。
- `http.client.HTTPConnection.connect()`：连接服务器。
- `http.client.HTTPConnection.close()`：关闭连接。
- `http.client.HTTPConnection.send(data)`：发送数据。
