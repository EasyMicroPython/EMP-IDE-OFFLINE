(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0ae57a"],{"0a3f":function(e,t,n){"use strict";n.r(t);n("3a0f"),n("a3a3"),n("4d0b");var o={methods:{SIGNAL_REPORT_CONNECTED:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"bottomBar",n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"slotConnected";return{event:"reportConnected",sender:e,receiver:t,slot:n,kwargs:{}}},SIGNAL_REPORT_DISCONNECTED:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"bottomBar",n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"slotDisconnected";return{event:"reportDisconnected",sender:e,receiver:t,slot:n,kwargs:{}}},SIGNAL_UPDATE_TREE:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:null,n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"folderTree",o=arguments.length>3&&void 0!==arguments[3]?arguments[3]:"slotUpdateTree";return{event:"updateTree",sender:e,receiver:n,slot:o,kwargs:{treeData:t}}},SIGNAL_UPDATE_FINDER:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:null,n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"finder",o=arguments.length>3&&void 0!==arguments[3]?arguments[3]:"slotUpdateFiles";return{event:"updateTree",sender:e,receiver:n,slot:o,kwargs:{files:t}}},SIGNAL_LOCK:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"parent",n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"slotLock";return{event:"lock",sender:e,receiver:t,slot:n,kwargs:{}}},SIGNAL_UNLOCK:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"parent",n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"slotUnlock";return{event:"unlock",sender:e,receiver:t,slot:n,kwargs:{}}},SIGNAL_SHOW_CODES:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:null,n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"editor",o=arguments.length>3&&void 0!==arguments[3]?arguments[3]:"slotShowCode";return{event:"showCode",sender:e,receiver:n,slot:o,kwargs:{code:t,filename:this.getFilename}}},SIGNAL_SHOW_CODES_PMAX:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:null,n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"editor",o=arguments.length>3&&void 0!==arguments[3]?arguments[3]:"slotShowCode";return{event:"showCode",sender:e,receiver:n,slot:o,kwargs:{code:t.code,filename:this.getFilename}}},SIGNAL_DEPENDS_ON_MEMORY_TO_GET_FILE:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:null,n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"self",o=arguments.length>3&&void 0!==arguments[3]?arguments[3]:"slotDependsOnMemoryToGetFile";return{event:"dependsOnMemoryToGetFile",sender:e,receiver:n,slot:o,kwargs:{mf:t.mf,fsize:t.fsize,filename:t.filename}}},SIGNAL_PUT_NEXT_FILE:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"uploader",n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"slotNextFile";return{event:"nextFile",sender:e,receiver:t,slot:n,kwargs:{}}},SIGNAL_SHOW_SYS_INFO:function(e,t){var n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"bottomBar",o=arguments.length>3&&void 0!==arguments[3]?arguments[3]:"slotShowSysInfo";return{event:"ShowSysInfo",sender:e,receiver:n,slot:o,kwargs:{data:t}}},SIGNAL_SHOW_MEMORY_STATUS:function(e,t){var n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"bottomBar",o=arguments.length>3&&void 0!==arguments[3]?arguments[3]:"slotShowMemoryStatus";return{event:"ShowMemoryStatus",sender:e,receiver:n,slot:o,kwargs:{data:t}}},SIGNAL_SHOW_PANE:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"splitVertical",n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"slotShowPane";return{event:"showPane",sender:e,receiver:t,slot:n,kwargs:{}}}}};t["default"]=o}}]);
//# sourceMappingURL=chunk-2d0ae57a.d2e4aa08.js.map