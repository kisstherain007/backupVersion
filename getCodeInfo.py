
from imp import reload
from xml.etree.ElementTree import ElementTree,Element
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def read_xml(in_path):
  tree = ElementTree()
  tree.parse(in_path)
  return tree

def find_nodes(tree, path):
  return tree.findall(path)

def get_node_by_keyvalue(nodelist, kv_map):
  result_nodes = []
  for node in nodelist:
    if if_match(node, kv_map):
      result_nodes.append(node)
  return result_nodes

def if_match(node, kv_map):
  for key in kv_map:
    if node.get(key) != kv_map.get(key):
      return False
  return True

def getReleaseBranchName(projectPath):
  stringsTree = read_xml(projectPath + "/res/values/strings.xml")
  stringsNode = find_nodes(stringsTree, "./string")
  result_stringNodes = get_node_by_keyvalue(stringsNode, {"name": "yiyuan_mingcheng"})
  for node in result_stringNodes:
    yiuanName = node.text

  manifestTree = read_xml(projectPath + "/AndroidManifest.xml")
  manifestNodes = find_nodes(manifestTree, ".")
  for node in manifestNodes:
    value = node.attrib["{http://schemas.android.com/apk/res/android}versionName"]
    # for attr in node.attrib:
    #   print(attr)
    version = value

  version = version.encode('utf-8')
  yiuanName = yiuanName.encode('utf-8')
  info_arr = []
  info_arr.append(version)
  info_arr.append(yiuanName)

  return info_arr