//导入默认导出
import myFunction1 from "./es6_module_export"

myFunction1()

//导入命名导出
import {myFunction2, myVariable} from "./es6_module_export";
myFunction2()
console.log(myVariable)

//导入所有导出
import * as myModule from "./es6_module_export";
myModule.func1()
myModule.func2()
