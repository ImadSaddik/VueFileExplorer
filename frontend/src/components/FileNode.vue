<template>
  <li>
    <div class="node-content">
      <span v-if="node.type === 'folder'" class="chevron" @click="toggle">
        {{ isOpen ? "▼" : "▶" }}
      </span>
      <span v-else class="spacer"></span>
      <span class="node-name" @click="toggle">
        {{ node.type === "folder" ? "📂" : "📄" }}
        {{ node.name }}
      </span>
    </div>
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
li {
  list-style-type: none;
}

ul {
  list-style: none;
  padding-left: 1.25rem;
  margin: 0;
}

.node-content {
  display: flex;
  align-items: center;
  padding: 0.25rem 0rem;
}

.node-content:hover {
  background-color: #306181;
  cursor: pointer;
}

.chevron {
  width: 1rem;
  font-size: 0.625rem;
  display: inline-block;
}

.spacer {
  width: 1rem;
  display: inline-block;
}

.node-name {
  margin-left: 0.25rem;
}
</style>
