/*
!! The feature that uses this endpoint has recently started rolling out to users.
!! See `App > Avatar > Profile Picture Editor`
!!
!! You may continue using this script, the only advantage is being able to
!! customize FullBody and Closeup independently.
*/



// ! VIEW YOUR CURRENT AVATAR THUMBNAIL CUSTOMIZATIONS: https://avatar.roblox.com/v1/avatar/thumbnail-customizations

/*
!! After your first time of setting a thumbnail configuration, the thumbnail of that type can not go back to how it was originally.
!! (i.e.: using Idle Animations, camera position). It can only be temporarily reverted if Roblox disables this feature again.
*/

// doing ajax because easy csrf handling w/their middleware lol
$.ajax({
    method: "POST",
    url: "https://avatar.roblox.com/v1/avatar/thumbnail-customization",
    contentType: "application/json",
    data: JSON.stringify({
      "camera": {
          // Ranges are inclusive.
          "distanceScale": 2, // 0.5 to 4 (Closeup) 1 (FullBody) - Camera distance scale from the avatar
          "fieldOfViewDeg": 30, // 15 to 45 - Camera Field Of View (FOV) in degrees, slight effect
          // xRotDeg used to exist here.
          "yRotDeg": 0 // -60 to 60 - Camera Y rotation in degrees
      },
      "emoteAssetId": 4646306072, /* The assetId of an emote you own. 0 for no emote. 
      * example: 3696763549 in https://www.roblox.com/catalog/3696763549/Heisman-Pose
      */
      // idleAnimationAssetId used to exist here, it has since been removed.
      "thumbnailType": 1 /* The thumbnailType
      * 1 = Closeup (headshot)
      * 2 = FullBody (bodyshot)
      
      Closeup and Fullbody can have separate configurations.
      */
    })
  }).then(data => console.log(data)).fail(error => alert(error.responseJSON.errors[0].message));
  // Logs `{success:true}` if success or website alert if error.