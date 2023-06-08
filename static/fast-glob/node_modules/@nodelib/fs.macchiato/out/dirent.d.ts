/// <reference types="node" />
import type * as fs from 'fs';
import type { PrepareOptionsFromClass } from './types';
export default class Dirent implements fs.Dirent {
    private readonly _options;
    readonly name: string;
    constructor(_options?: PrepareOptionsFromClass<fs.Dirent>);
    isFile(): boolean;
    isDirectory(): boolean;
    isBlockDevice(): boolean;
    isCharacterDevice(): boolean;
    isSymbolicLink(): boolean;
    isFIFO(): boolean;
    isSocket(): boolean;
}
