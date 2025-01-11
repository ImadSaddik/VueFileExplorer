<template>
  <div class="file-explorer">
    <ul>
      <FileNode v-for="(node, index) in fileTree" :key="index" :node="node" />
    </ul>
  </div>
</template>

<script>
import fileTreeData from "@/assets/file_tree.json";
import FileNode from "@/components/FileNode.vue";

export default {
  name: "FileExplorer",
  components: {
    FileNode,
  },
  data() {
    return {
      fileTree: fileTreeData,
    };
  },
};
</script>
