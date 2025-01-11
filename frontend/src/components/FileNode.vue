<template>
  <li>
    <span @click="toggle">
      {{ node.type === "folder" ? (isOpen ? "📂" : "📁") : "📄" }}
      {{ node.name }}
    </span>
    <ul v-if="node.children && isOpen">
      <FileNode
        v-for="(child, index) in node.children"
        :key="index"
        :node="child"
      />
    </ul>
  </li>
</template>

<script>
export default {
  name: "FileNode",
  props: {
    node: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      isOpen: false,
    };
  },
  methods: {
    toggle() {
      if (this.node.type === "folder") {
        this.isOpen = !this.isOpen;
      }
    },
  },
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 20px;
}

li span {
  cursor: pointer;
}

li span:hover {
  color: #007acc;
}
</style>
