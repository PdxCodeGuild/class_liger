
# Lab 5: Random Quote


Use the [favqs.com](https://favqs.com/api/) api to show a random quote. To start, use `https://favqs.com/api/qotd` to `GET` a quote, then display it on the page.

```json
{
  "id": 4,
  "author": "Albert Einstein",
  "body": "Make everything as simple as possible, but not simpler.",
  ...
}
```


## Version 2

The API also supports browsing quotes. 

You will need to sign up for an account, visit the API link at the very bottom of the page and generate an API key. The key will act like a username/password and authorize your API request when searching for quotes.

## **Never commit API keys to Github!**

There are bots that crawl Github looking for API keys to steal. If you publish a key for an API that costs money and someone steals and uses it, *you* will be responsible for the charges.

To keep it safe, we'll put the key in a file called `secrets.js` which will be included in a `<script>` tag before the main Javascript file in `index.html`.

### secrets.js
```javascript

// replace with your API key as a string
const FAVQS_API_KEY = 'ab09c7b09c7ca9c7b9ca0c79c7b97cb' 

```

### index.html
```html
<body>
    ...

    <script src="secrets.js"></script>
    <script src="index.js"></script>
</body>
```

As long as `secrets.js` is loaded before `index.js`, the API key variable will be available.

The API key will be included in the headers object that's passed to the API along with your request. The authorization header will have to be formatted like so: 

```javascript
const headers = {
    // ... other headers

    Authorization: `Token token=${API_KEY_HERE}`
}
```

**Note:** This is still not the most secure way to handle secret keys. We'll see other ways later in the course.

You can use Favqs' `page` and `filter` parameters to get a bunch of quotes from the API. You can add page buttons and a text `input` field and `button` for filtering.

Provide URL parameters for your request either by including them in the URL using template literal syntax

```javascript
// notice that the base url changes from /api/qotd to /api/quotes
const url = `https://favqs.com/api/quotes?page=${pageNumber}&filter=${queryString}`
```

or via Axios' `params` option that can be included next to the `headers` object.

```javascript
const params = {
    page: pageNumber,
    filter: queryString
}

axios.get(
    url,
    {
        headers: headers,
        params: params
    }
)
```

This will return data with a **list of quotes**, the **current page number** and a **boolean indicating whether or not it is the last page of quotes for that search**.