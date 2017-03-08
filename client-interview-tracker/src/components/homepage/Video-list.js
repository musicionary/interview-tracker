import React from 'react';
import VideoListItems from './Video-list-items';


const VideoList = (props) => {

  const videos = props.videos.map((video) => {
    return (
      <VideoListItems
        onVideoSelect={props.onVideoSelect}
        key={video.etag}
        video={video} />
    )
  });

  return (
    <ul className="col-md-4 list-group">
      {videos}
    </ul>
  );
};

export default VideoList;
