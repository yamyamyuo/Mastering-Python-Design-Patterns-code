# conding:utf-8
import pprint # 美化输出
from collections import namedtuple
from operator import attrgetter # 生成按名称提取属性的函数
if __name__ == '__main__':
    ProgrammingLang = namedtuple('ProgrammingLang', 'name ranking')
    stats = (('Ruby', 14), ('Javascript', 8), ('Python', 7),
             ('Scala', 31), ('Swift', 18), ('Lisp', 23))
    lang_stats = [ProgrammingLang(n, r) for n, r in stats]
    pp = pprint.PrettyPrinter(indent=5)
    pp.pprint(sorted(lang_stats, key=attrgetter('name')))
    print()
    pp.pprint(sorted(lang_stats, key=attrgetter('ranking')))
