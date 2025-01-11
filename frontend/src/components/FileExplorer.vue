<template>
  <div class="file-explorer">
    <ul>
      <FileNode
        v-for="(node, index) in fileTree"
        :key="index"
        :node="node"
        :max-depth="maxDepth"
        :level="1"
      />
    </ul>
  </div>
</template>

<script>
import fileTreeData from "@/assets/file_tree.json";
import FileNode from "@/components/FileNode.vue";

export default {
  name: "FileExplorer",
  props: {
    maxDepth: {
      type: Number,
      default: -1,
    },
  },
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

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0;
}
</style>
