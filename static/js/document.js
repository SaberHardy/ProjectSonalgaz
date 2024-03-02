function uploadFile() {
  const fileInput = document.getElementById('fileInput');
  const fileList = fileInput.files;

  if (fileList.length > 0) {
      const file = fileList[0];
      const downloadLinks = document.getElementById('downloadLinks');
      const fileURL = URL.createObjectURL(file);
      const link = document.createElement('a');
      
      link.href = fileURL;
      link.download = file.name;
      link.innerHTML = file.name;
      
      downloadLinks.appendChild(link);
  } else {
      alert('Please select a file to upload.');
  }
}
