window.onload = () => {
  $("#sendbutton").click(() => {
    $body = $("body");
    imagebox = $("#imagebox");
    link = $("#link");
    input = $("#imageinput")[0];
    if (input.files && input.files[0]) {
      console.log(input.files[0])
      let formData = new FormData();
      formData.append("video", input.files[0]);
      $.ajax({
        url: "/detect", // fix this to your liking
        type: "POST",
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        error: function (data) {
          console.log("upload error", data);
          console.log(data.getAllResponseHeaders());
        },
        success: function (data) {
          // bytestring = data["status"];
          // image = bytestring.split("'")[1];
          $("#link").css("visibility", "visible");
          // // $("#download").attr("href", data);
          document.getElementById('original').src = 'data:;base64,' + data['image_original'];
          document.getElementById('preprocessing').src = 'data:;base64,' + data['image_preprocessing'];
          document.getElementById('augmented').src = 'data:;base64,' + data['image_augemented'];
          // $("#download").attr("src",data);
          console.log(data)
        },
      });
    }
  });
};

function readUrl(input) {
  imagebox = $("#imagebox");
  console.log(imagebox);
  console.log("evoked readUrl");
  console.log(input.files[0]);
  if (input.files && input.files[0]) {
    let reader = new FileReader();
    reader.onload = function (e) {
      console.log(e.target);

      imagebox.attr("src", e.target.result);
      //   imagebox.height(500);
      //   imagebox.width(800);
    };
    // const img = Image();
    // img.src= reader.result;
    // document.body.appendChild(img);
    reader.readAsDataURL(input.files[0]);
  }
}
