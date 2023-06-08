# Installation
> `npm install --save @types/glob-parent`

# Summary
This package contains type definitions for glob-parent (https://github.com/gulpjs/glob-parent).

# Details
Files were exported from https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/glob-parent.
## [index.d.ts](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/glob-parent/index.d.ts)
````ts
// Type definitions for glob-parent 5.1
// Project: https://github.com/gulpjs/glob-parent
// Definitions by: mrmlnc <https://github.com/mrmlnc>
// Definitions: https://github.com/DefinitelyTyped/DefinitelyTyped

declare function globParent(pattern: string, options?: globParent.Options): string;

declare namespace globParent {
    interface Options {
        flipBackslashes?: boolean | undefined;
    }
}

export = globParent;

````

### Additional Details
 * Last updated: Tue, 06 Jul 2021 20:33:05 GMT
 * Dependencies: none
 * Global values: none

# Credits
These definitions were written by [mrmlnc](https://github.com/mrmlnc).
