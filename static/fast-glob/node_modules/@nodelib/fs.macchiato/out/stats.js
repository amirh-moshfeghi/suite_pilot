"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const uid = process.platform === 'win32' ? undefined : process.getuid();
const gid = process.platform === 'win32' ? undefined : process.getgid();
class Stats {
    constructor(_options = {}) {
        var _a, _b, _c, _d, _e, _f, _g, _h, _j, _k, _l, _m, _o, _p, _q, _r;
        this._options = _options;
        this._date = new Date();
        this.dev = (_a = this._options.dev) !== null && _a !== void 0 ? _a : 0;
        this.ino = (_b = this._options.ino) !== null && _b !== void 0 ? _b : 0;
        this.mode = (_c = this._options.mode) !== null && _c !== void 0 ? _c : 0;
        this.nlink = (_d = this._options.nlink) !== null && _d !== void 0 ? _d : 0;
        this.uid = ('uid' in this._options ? this._options.uid : uid);
        this.gid = ('gid' in this._options ? this._options.gid : gid);
        this.rdev = (_e = this._options.rdev) !== null && _e !== void 0 ? _e : 0;
        this.size = (_f = this._options.size) !== null && _f !== void 0 ? _f : 0;
        this.blksize = (_g = this._options.blksize) !== null && _g !== void 0 ? _g : 0;
        this.blocks = (_h = this._options.blocks) !== null && _h !== void 0 ? _h : 0;
        this.atimeMs = (_j = this._options.atimeMs) !== null && _j !== void 0 ? _j : this._date.getTime();
        this.mtimeMs = (_k = this._options.mtimeMs) !== null && _k !== void 0 ? _k : this._date.getTime();
        this.ctimeMs = (_l = this._options.ctimeMs) !== null && _l !== void 0 ? _l : this._date.getTime();
        this.birthtimeMs = (_m = this._options.birthtimeMs) !== null && _m !== void 0 ? _m : this._date.getTime();
        this.atime = (_o = this._options.atime) !== null && _o !== void 0 ? _o : this._date;
        this.mtime = (_p = this._options.mtime) !== null && _p !== void 0 ? _p : this._date;
        this.ctime = (_q = this._options.ctime) !== null && _q !== void 0 ? _q : this._date;
        this.birthtime = (_r = this._options.birthtime) !== null && _r !== void 0 ? _r : this._date;
    }
    isFile() {
        var _a;
        return (_a = this._options.isFile) !== null && _a !== void 0 ? _a : true;
    }
    isDirectory() {
        var _a;
        return (_a = this._options.isDirectory) !== null && _a !== void 0 ? _a : false;
    }
    isBlockDevice() {
        var _a;
        return (_a = this._options.isBlockDevice) !== null && _a !== void 0 ? _a : false;
    }
    isCharacterDevice() {
        var _a;
        return (_a = this._options.isCharacterDevice) !== null && _a !== void 0 ? _a : false;
    }
    isSymbolicLink() {
        var _a;
        return (_a = this._options.isSymbolicLink) !== null && _a !== void 0 ? _a : false;
    }
    isFIFO() {
        var _a;
        return (_a = this._options.isFIFO) !== null && _a !== void 0 ? _a : false;
    }
    isSocket() {
        var _a;
        return (_a = this._options.isSocket) !== null && _a !== void 0 ? _a : false;
    }
}
exports.default = Stats;
