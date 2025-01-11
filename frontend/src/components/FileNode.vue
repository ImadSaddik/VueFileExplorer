<template>
  <li>
    <div class="node-content">
      <span v-if="node.type === 'folder'" class="chevron" @click="toggle">
        {{ isOpen ? "▼" : "▶" }}
      </span>
      <span v-else class="spacer"></span>
      <span class="node-name" @click="toggle">
        <img
          v-if="node.type === 'file'"
          :src="getFileIcon"
          class="file-icon"
          alt="file icon"
        />
        <span v-else>📂</span>
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
import cssIcon from "@/assets/icons/css.svg";
import csvIcon from "@/assets/icons/csv.svg";
import docIcon from "@/assets/icons/doc.svg";
import fileIcon from "@/assets/icons/file.svg";
import gitIcon from "@/assets/icons/git.svg";
import htmlIcon from "@/assets/icons/html.svg";
import icoIcon from "@/assets/icons/ico.svg";
import jsIcon from "@/assets/icons/javascript.svg";
import jsonIcon from "@/assets/icons/json.svg";
import jpgIcon from "@/assets/icons/jpg.svg";
import mdIcon from "@/assets/icons/md.svg";
import pngIcon from "@/assets/icons/png.svg";
import pptIcon from "@/assets/icons/ppt.svg";
import pythonIcon from "@/assets/icons/python.svg";
import svgIcon from "@/assets/icons/svg.svg";
import txtIcon from "@/assets/icons/txt.svg";
import vueIcon from "@/assets/icons/vue.svg";
import xlsIcon from "@/assets/icons/xls.svg";
import xmlIcon from "@/assets/icons/xml.svg";
import zipIcon from "@/assets/icons/zip.svg";

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
      defaultIcon: fileIcon,
    };
  },
  computed: {
    getFileIcon() {
      if (this.node.type === "folder") return null;

      const ext = this.node.name.split(".").pop().toLowerCase();
      const iconMap = {
        css: cssIcon,
        csv: csvIcon,
        doc: docIcon,
        docx: docIcon,
        file: fileIcon,
        git: gitIcon,
        gitignore: gitIcon,
        html: htmlIcon,
        ico: icoIcon,
        js: jsIcon,
        jsx: jsIcon,
        json: jsonIcon,
        jpg: jpgIcon,
        jpeg: jpgIcon,
        md: mdIcon,
        png: pngIcon,
        ppt: pptIcon,
        pptx: pptIcon,
        py: pythonIcon,
        svg: svgIcon,
        txt: txtIcon,
        vue: vueIcon,
        xls: xlsIcon,
        xlsx: xlsIcon,
        xml: xmlIcon,
        zip: zipIcon,
        tar: zipIcon,
        gz: zipIcon,
      };

      return iconMap[ext] || this.defaultIcon;
    },
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
  position: relative;
}

ul {
  list-style: none;
  padding-left: 1.25rem;
  margin: 0;
  position: relative;
}

ul::before {
  content: "";
  position: absolute;
  left: 0.25rem;
  top: 0;
  height: 100%;
  border-left: 1px solid #ccc;
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

.file-icon {
  width: 16px;
  height: 16px;
  vertical-align: middle;
  margin-right: 4px;
}
</style>
