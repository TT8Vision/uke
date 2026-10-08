# Product source files

One JSON file per product, named by its id (`uke-0001.json`). **These files
are the source of truth for the catalogue.**

The site does not read them directly. It reads `data/products.json`, which is
generated from these files:

```
npm run build:catalogue
```

Run that after any edit here and commit both the edited file and the
regenerated `data/products.json`. Netlify also runs it on every deploy.

## Fields

| field        | meaning                                                  |
|--------------|----------------------------------------------------------|
| `id`         | must match the filename, e.g. `uke-0869`                 |
| `brand`      | brand name shown on the card                             |
| `name`       | product name                                             |
| `volume`     | pack size text, or `null` to hide it                     |
| `price`      | number in rand, e.g. `84.9` (never a string)             |
| `oldPrice`   | number shown struck through, or `null`                   |
| `sku`        | optional stock code, or `null`                           |
| `image`      | local path, e.g. `images/products/uke-0001.webp`         |
| `categories` | list of category keys, e.g. `["beers"]`                  |
| `tag`        | badge text such as `"Sale"`, or `null`                   |
| `inStock`    | `true` / `false`                                         |
| `new`        | `true` to feature in the homepage "new" strip            |
| `dateAdded`  | `YYYY-MM-DD`                                             |

Category keys in use: beers, cereals, cleaning, colddrinks, confectionery,
groceries, hotdrinks, kent, personalcare.

New products take the next unused id: one higher than the highest existing
`uke-####` file.
