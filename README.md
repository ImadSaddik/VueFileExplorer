# Vue - File explorer

I am recreating the file explorer from VS Code just for fun. I'm building it with Vue.js, my favorite web framework. I'm using Python to generate the file tree that Vue.js needs to build the explorer.

## Demo

- **Quick preview**  
  ![Video preview](https://github.com/ImadSaddik/VueFileExplorer/blob/main/videos/demo.webm)

- **Side-by-Side comparison**  
  ![Side by Side comparison](/images/comparison.svg)

## Getting started

### Step 1: Generate the file tree

To generate the file tree, navigate to the `backend` directory and execute `main.py`:

```bash
python main.py
```

The script will create a file tree structure for the entire project, which will look something like this:

```json
[
  {
    "name": "backend",
    "type": "folder",
    "children": [
      {
        "name": "file_tree.json",
        "type": "file"
      },
      {
        "name": "main.py",
        "type": "file"
      }
    ]
  },
  {
    "name": ".gitignore",
    "type": "file"
  },
  ...
]
```

### File tree structure

Each item in the file tree can either be a `file` or a `folder`. Folders include a `children` field, listing their contents.  
For example:

- A `file` item contains the `name` and `type` fields.  
- If you wish to include file content, add a `content` field in the `main.py` script.

### Step 2: View the file tree

Once the file tree is generated, navigate to the `frontend` folder and run the following commands:

```bash
npm install
npm run serve
```

Then, open the development server in your browser and explore!

## Contributing

Contributions are highly encouraged!  
Feel free to:

1. Fork the repository.
2. Make improvements or add features.
3. Submit a pull request.

## Contact

- **Email**: [simad3647@gmail.com](mailto:simad3647@gmail.com)  
- **LinkedIn**: [Imad Saddik](https://www.linkedin.com/in/imadsaddik/)
