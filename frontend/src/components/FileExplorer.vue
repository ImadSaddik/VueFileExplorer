<template>
  <div class="file-explorer">
    <ul>
      <FileNode
        v-for="(node, index) in sortedFileTree"
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
  computed: {
    sortedFileTree() {
      return [...this.fileTree].sort((a, b) => {
        // If both are same type, sort alphabetically
        if (a.type === b.type) {
          return a.name.toLowerCase().localeCompare(b.name.toLowerCase());
        }
        // If different types, folders come first
        return a.type === "folder" ? -1 : 1;
      });
    },
  },
};
</script>

<style scoped>
.file-explorer {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  overflow-x: hidden;
  overflow-y: auto;
  border: 1px solid #e0e0e0;
}

ul {
  list-style-type: none;
  padding-left: 0;
  margin: 0;
  width: 100%;
}
</style>
