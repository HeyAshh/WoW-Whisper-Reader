const { spawn } = require('child_process');
const py = spawn('python', ['path/to/opencv_script.py']);

py.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

py.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

py.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});

// send data to the Python script
py.stdin.write(JSON.stringify({ message: 'hello from Electron' }));
py.stdin.end();
