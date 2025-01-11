<template>Hi world</template>

<script>
import fileTreeData from "@/assets/file_tree.json";

export default {
  name: "FileExplorer",
  components: {},
  data() {
    return {
      fileTree: fileTreeData,
    };
  },
};
</script>
