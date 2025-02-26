// 浏览器存储 local、cookie、session、IndexedDB
localStorage.setItem('name', 'John'); // 存储数据
console.log(localStorage.getItem('name')); // 获取数据
localStorage.removeItem('name'); // 删除数据

// cookie
document.cookie = "name=John"; // 存储数据
console.log(document.cookie); // 获取数据
document.cookie = "name=;expires=Thu, 01 Jan 1970 00:00:00 UTC"; // 删除数据

// sessionStorage
sessionStorage.setItem('name', 'John'); // 存储数据
console.log(sessionStorage.getItem('name')); // 获取数据
sessionStorage.removeItem('name'); // 删除数据

// IndexedDB
// 创建数据库
var db = new IndexedDB('myDB', 1);

// 定义对象仓库
var objectStore = db.createObjectStore('myObjectStore', { keyPath: 'id', autoIncrement: true });
// 存储数据
var transaction = db.transaction(['myObjectStore'],'readwrite');
var objectStore = transaction.objectStore('myObjectStore');
objectStore.add({ name: 'John' });

// 获取数据
var transaction = db.transaction(['myObjectStore'],'readonly');
var objectStore = transaction.objectStore('myObjectStore');
var request = objectStore.get(1);
request.onsuccess = function(event) {
  console.log(request.result.name);
};

// 关闭数据库
db.close();