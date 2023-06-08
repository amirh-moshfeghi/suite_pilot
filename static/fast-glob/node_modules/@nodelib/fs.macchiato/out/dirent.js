"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
class Dirent {
    constructor(_options = {}) {
        var _a;
        this._options = _options;
        this.name = (_a = this._options.name) !== null && _a !== void 0 ? _a : 'unknown.txt';
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
exports.default = Dirent;
