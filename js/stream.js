document.addEventListener("DOMContentLoaded", () => {
    const video = document.querySelector("video");
    const source = video.getElementsByTagName("source")[0].src;
    const defaultOptions = {};
    let hls;

    if (Hls.isSupported()) {
      hls = new Hls();
      hls.loadSource(source);
      hls.on(Hls.Events.MANIFEST_PARSED, function (event, data) {
        const availableQualities = hls.levels.map((l) => l.height);
        defaultOptions.quality = {
          default: availableQualities[0],
          options: availableQualities,
          forced: true,
          onChange: (e) => updateQuality(e),
        };
        initializePlyr(video, defaultOptions, hls);
      });
      hls.attachMedia(video);
      window.hls = hls;
    } else {
      initializePlyr(video, defaultOptions);
    }

    function initializePlyr(video, options, hls) {
      const player = new Plyr(video, options);
      player.on("languagechange", () => {
        setTimeout(() => {
          if (hls) {
            hls.subtitleTrack = player.currentTrack;
          }
        }, 50);
      });
    }

    function updateQuality(newQuality) {
      window.hls.levels.forEach((level, levelIndex) => {
        if (level.height === newQuality) {
          console.log("Found quality match with " + newQuality);
          window.hls.currentLevel = levelIndex;
        }
      });
    }
  });