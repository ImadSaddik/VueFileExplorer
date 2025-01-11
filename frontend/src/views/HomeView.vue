<template>
  <div>
    <FileExplorer :maxDepth="-1" style="width: 20rem" />
  </div>
</template>

<script>
import FileExplorer from "@/components/FileExplorer.vue";
export default {
  name: "HomeView",
  components: {
    FileExplorer,
  },
};
</script>
