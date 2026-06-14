import "./index.css";
import { Composition } from "remotion";
import { KordovanAd } from "./KordovanAd";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="KordovanAd"
        component={KordovanAd}
        durationInFrames={450}
        fps={30}
        width={1080}
        height={1920}
      />
    </>
  );
};
