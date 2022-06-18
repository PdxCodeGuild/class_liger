# Markdown Intro

# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5

Alternative h1 underline-style header
===

Alternatate h2 underline-style header
---

---

## Emphasis
This will be *italic*. This will also be _italic_

This will be **bold**. This will also be __bold__

This will be **_italic and bold_**.

This will be ~~strikethrough~~ 

## Lists
1. Red
2. Green
3. Blue
---
1. Red
   1. Green
   2. Blue
---
* Red
* Green
* Blue
---
* Red
  * Green
  * Blue
---
1. Red
    * Green
    * Blue
---
## Checkboxes
- [ ] task 1
- [ ] task 2
- [x] task 3
- [ ] task 4
---

## Links
[About](about.md)

[Google](http://google.com)

![JavaScript Logo](./images/JavaScript-Logo.png)

<img src="./images/JavaScript-Logo.png" width=100 />

---

## Syntax Highlighting

Inline code uses single back-ticks 
Execute a `print()` function in Python.

```
# For larger code blocks, use triple back ticks

x = 5

print(x)
```

### Python code
```python
def add(a, b):
    return a + b

print(add(2, 2))
```

### JavaScript code
```javascript
function add(a, b){
    return a + b
}

console.log(add(2, 2))
```

### JSON data
```JSON
[
  {
    "title": "apples",
    "count": [12000, 20000],
    "description": {"text": "...", "sensitive": false}
  },
  {
    "title": "oranges",
    "count": [17500, null],
    "description": {"text": "...", "sensitive": false}
  }
]
```

---

## Tables
|Column 1| Column 2| Column 3|
|--------|---------|---------|
|1,1     | 1,2     | 1,3     |
|2,1     | 2,2     | 2,3     |
|3,1     | 3,2     | 3,3     |

---

## Dropdowns
<details open>
<summary>Dropdown 1</summary>

   - item 1
   - item 2
   - item 3

</details>

