const express = require('express');
const router = express.Router()
var fs = require('fs');
var exec = require('child_process').exec;

function execute(command, callback){
    exec(command, function(error, stdout, stderr){ callback(stdout); });
};

var compile = function(req, res){
  fs.writeFile('Tests/InterfaceCode.txt', req.body.data, function (err) {
    if (err){res.send("ERROR")};
  });
  execute("python IntermediateCode.py", function(compileCode){
    res.send({"response": compileCode})
  });
}

router.post('/compile', compile);
router.get('*', function(req, res) {res.send({error: 'Route does not exist'})})

module.exports = router;