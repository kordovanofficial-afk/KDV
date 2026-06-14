import React from "react";
import {
  AbsoluteFill,
  Easing,
  Sequence,
  interpolate,
  useCurrentFrame,
} from "remotion";

// ─── Helpers ─────────────────────────────────────────────────────────────────

function easeOut(frame: number, start: number, end: number): number {
  return interpolate(frame, [start, end], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });
}


// ─── Design tokens ───────────────────────────────────────────────────────────

const GOLD = "#C9A84C";
const CREAM = "#F5EED7";
const DARK = "#0A0704";
const BROWN = "#3B1F0E";

// ─── Particle dots ───────────────────────────────────────────────────────────

const PARTICLES = Array.from({ length: 28 }, (_, i) => ({
  id: i,
  x: (i * 137.5) % 100,
  y: (i * 73.3) % 100,
  size: 1.5 + (i % 4) * 0.8,
  delay: (i * 7) % 40,
  speed: 60 + (i % 5) * 20,
}));

const Particles: React.FC = () => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{ overflow: "hidden", pointerEvents: "none" }}>
      {PARTICLES.map((p) => {
        const progress = ((frame + p.delay * 2) % p.speed) / p.speed;
        const opacity = interpolate(
          progress,
          [0, 0.2, 0.8, 1],
          [0, 0.6, 0.6, 0],
          { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
        );
        const translateY = interpolate(progress, [0, 1], [0, -60], {
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
        });
        return (
          <div
            key={p.id}
            style={{
              position: "absolute",
              left: `${p.x}%`,
              top: `${p.y}%`,
              width: p.size,
              height: p.size,
              borderRadius: "50%",
              background: GOLD,
              opacity,
              transform: `translateY(${translateY}px)`,
            }}
          />
        );
      })}
    </AbsoluteFill>
  );
};

// ─── Animated line divider ────────────────────────────────────────────────────

const GoldLine: React.FC<{ frame: number; startFrame: number }> = ({
  frame,
  startFrame,
}) => {
  const width = interpolate(frame, [startFrame, startFrame + 25], [0, 180], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });
  return (
    <div
      style={{
        height: 2,
        width,
        background: `linear-gradient(90deg, ${GOLD}, transparent)`,
        marginTop: 12,
        marginBottom: 12,
      }}
    />
  );
};

// ─── Scene 1 — Brand Reveal (0–4s = 0–120f) ──────────────────────────────────

const Scene1: React.FC = () => {
  const frame = useCurrentFrame();

  const bgScale = interpolate(frame, [0, 120], [1.08, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.quad),
  });

  const logoOpacity = easeOut(frame, 20, 60);
  const logoY = interpolate(frame, [20, 60], [40, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  const taglineOpacity = easeOut(frame, 55, 90);
  const taglineY = interpolate(frame, [55, 90], [30, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  const lineOpacity = easeOut(frame, 48, 70);

  // vignette fade-in
  const vignetteOpacity = easeOut(frame, 0, 40);

  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(ellipse at 30% 40%, ${BROWN} 0%, ${DARK} 70%)`,
        transform: `scale(${bgScale})`,
        transformOrigin: "center center",
      }}
    >
      {/* Grain texture overlay */}
      <AbsoluteFill
        style={{
          background:
            "url(\"data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E\")",
          backgroundSize: "200px 200px",
          opacity: 0.3,
          mixBlendMode: "overlay",
        }}
      />

      {/* Vignette */}
      <AbsoluteFill
        style={{
          background:
            "radial-gradient(ellipse at center, transparent 40%, rgba(0,0,0,0.75) 100%)",
          opacity: vignetteOpacity,
        }}
      />

      {/* Horizontal gold accent lines */}
      <div
        style={{
          position: "absolute",
          top: "12%",
          left: 80,
          right: 80,
          height: 1,
          background: `linear-gradient(90deg, transparent, ${GOLD}44, transparent)`,
          opacity: lineOpacity,
        }}
      />
      <div
        style={{
          position: "absolute",
          bottom: "12%",
          left: 80,
          right: 80,
          height: 1,
          background: `linear-gradient(90deg, transparent, ${GOLD}44, transparent)`,
          opacity: lineOpacity,
        }}
      />

      <Particles />

      {/* Logo / Brand name */}
      <AbsoluteFill
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          gap: 0,
        }}
      >
        {/* K monogram circle */}
        <div
          style={{
            opacity: logoOpacity,
            transform: `translateY(${logoY}px)`,
            marginBottom: 32,
          }}
        >
          <div
            style={{
              width: 120,
              height: 120,
              borderRadius: "50%",
              border: `2px solid ${GOLD}`,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              background: "rgba(201,168,76,0.07)",
            }}
          >
            <span
              style={{
                fontFamily: "Georgia, serif",
                fontSize: 64,
                color: GOLD,
                fontWeight: 700,
                letterSpacing: -2,
                lineHeight: 1,
              }}
            >
              K
            </span>
          </div>
        </div>

        <div
          style={{
            opacity: logoOpacity,
            transform: `translateY(${logoY}px)`,
          }}
        >
          <div
            style={{
              fontFamily: "Georgia, 'Times New Roman', serif",
              fontSize: 72,
              fontWeight: 700,
              color: CREAM,
              letterSpacing: 12,
              textTransform: "uppercase",
              textAlign: "center",
            }}
          >
            KORDOVAN
          </div>
        </div>

        <div
          style={{
            opacity: taglineOpacity,
            transform: `translateY(${taglineY}px)`,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          <div
            style={{
              width: 180,
              height: 1,
              background: `linear-gradient(90deg, transparent, ${GOLD}, transparent)`,
              margin: "16px 0",
            }}
          />
          <div
            style={{
              fontFamily: "Georgia, serif",
              fontSize: 22,
              color: GOLD,
              letterSpacing: 8,
              textTransform: "uppercase",
            }}
          >
            LEATHER
          </div>
        </div>

        <div
          style={{
            opacity: taglineOpacity,
            transform: `translateY(${taglineY}px)`,
            marginTop: 28,
          }}
        >
          <div
            style={{
              fontFamily: "'Helvetica Neue', Arial, sans-serif",
              fontSize: 20,
              color: `${CREAM}99`,
              letterSpacing: 4,
              textTransform: "uppercase",
            }}
          >
            Crafted to Last a Lifetime
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// ─── Scene 2 — Product Focus (120–255f = 4–8.5s) ─────────────────────────────

const Scene2: React.FC = () => {
  const frame = useCurrentFrame();

  const slideIn = easeOut(frame, 0, 35);
  const contentIn = easeOut(frame, 20, 55);

  // Animated shimmer
  const shimmerX = interpolate(frame, [0, 135], [-200, 1400], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{ background: DARK, overflow: "hidden" }}>
      {/* Background leather texture pattern */}
      <AbsoluteFill
        style={{
          background: `
            repeating-linear-gradient(
              45deg,
              transparent,
              transparent 8px,
              rgba(201,168,76,0.015) 8px,
              rgba(201,168,76,0.015) 16px
            )
          `,
        }}
      />

      {/* Left gold accent bar */}
      <div
        style={{
          position: "absolute",
          left: 0,
          top: 0,
          bottom: 0,
          width: interpolate(frame, [0, 30], [0, 6], {
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
            easing: Easing.bezier(0.16, 1, 0.3, 1),
          }),
          background: `linear-gradient(180deg, transparent, ${GOLD}, transparent)`,
        }}
      />

      {/* Product image placeholder — elegant dark card */}
      <div
        style={{
          position: "absolute",
          top: "10%",
          left: "8%",
          right: "8%",
          height: "52%",
          borderRadius: 16,
          background: `linear-gradient(135deg, ${BROWN}CC 0%, #1a0c04 100%)`,
          border: `1px solid ${GOLD}33`,
          opacity: slideIn,
          transform: `translateY(${interpolate(frame, [0, 35], [60, 0], {
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
            easing: Easing.bezier(0.16, 1, 0.3, 1),
          })}px)`,
          overflow: "hidden",
          boxShadow: "0 40px 80px rgba(0,0,0,0.6)",
        }}
      >
        {/* Shimmer effect */}
        <div
          style={{
            position: "absolute",
            top: 0,
            bottom: 0,
            left: shimmerX,
            width: 200,
            background:
              "linear-gradient(90deg, transparent, rgba(201,168,76,0.15), transparent)",
            transform: "skewX(-20deg)",
          }}
        />

        {/* Inner leather grain pattern */}
        <div
          style={{
            position: "absolute",
            inset: 0,
            background: `
              radial-gradient(ellipse at 30% 30%, rgba(201,168,76,0.12) 0%, transparent 60%),
              radial-gradient(ellipse at 70% 70%, rgba(59,31,14,0.8) 0%, transparent 50%)
            `,
          }}
        />

        {/* Wallet illustration via CSS */}
        <div
          style={{
            position: "absolute",
            top: "50%",
            left: "50%",
            transform: "translate(-50%, -50%)",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 12,
          }}
        >
          {/* Wallet body */}
          <div
            style={{
              width: 280,
              height: 180,
              borderRadius: 18,
              background: `linear-gradient(145deg, #5C3317 0%, #3B1F0E 100%)`,
              border: `1px solid ${GOLD}66`,
              position: "relative",
              boxShadow: "0 20px 60px rgba(0,0,0,0.5), inset 0 1px 0 rgba(201,168,76,0.3)",
            }}
          >
            {/* Wallet fold line */}
            <div
              style={{
                position: "absolute",
                left: "50%",
                top: 8,
                bottom: 8,
                width: 1,
                background: `linear-gradient(180deg, transparent, ${GOLD}44, transparent)`,
              }}
            />
            {/* Card slots */}
            {[0, 1, 2].map((i) => (
              <div
                key={i}
                style={{
                  position: "absolute",
                  left: 16 + i * 4,
                  top: 20 + i * 6,
                  width: 100,
                  height: 60,
                  borderRadius: 6,
                  background: `rgba(201,168,76,${0.06 + i * 0.02})`,
                  border: `1px solid ${GOLD}22`,
                }}
              />
            ))}
            {/* Monogram */}
            <div
              style={{
                position: "absolute",
                right: 24,
                bottom: 18,
                fontFamily: "Georgia, serif",
                fontSize: 28,
                color: `${GOLD}88`,
                fontWeight: 700,
                letterSpacing: 2,
              }}
            >
              K
            </div>
          </div>
          <div
            style={{
              fontFamily: "Georgia, serif",
              fontSize: 16,
              color: `${GOLD}66`,
              letterSpacing: 4,
              textTransform: "uppercase",
            }}
          >
            Bifold Wallet
          </div>
        </div>
      </div>

      {/* Text content */}
      <div
        style={{
          position: "absolute",
          bottom: "8%",
          left: "8%",
          right: "8%",
          opacity: contentIn,
          transform: `translateY(${interpolate(frame, [20, 55], [40, 0], {
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
            easing: Easing.bezier(0.16, 1, 0.3, 1),
          })}px)`,
        }}
      >
        <div
          style={{
            fontFamily: "'Helvetica Neue', Arial, sans-serif",
            fontSize: 16,
            color: GOLD,
            letterSpacing: 6,
            textTransform: "uppercase",
            marginBottom: 12,
          }}
        >
          New Arrival
        </div>
        <div
          style={{
            fontFamily: "Georgia, 'Times New Roman', serif",
            fontSize: 52,
            fontWeight: 700,
            color: CREAM,
            lineHeight: 1.1,
            marginBottom: 8,
          }}
        >
          Full-Grain
          <br />
          Leather Wallet
        </div>
        <GoldLine frame={frame} startFrame={30} />
        <div
          style={{
            fontFamily: "'Helvetica Neue', Arial, sans-serif",
            fontSize: 22,
            color: `${CREAM}BB`,
            lineHeight: 1.6,
          }}
        >
          Handcrafted in Pakistan.
          <br />
          Built to age beautifully.
        </div>
      </div>

      <Particles />
    </AbsoluteFill>
  );
};

// ─── Scene 3 — Feature Pills (255–360f = 8.5–12s) ────────────────────────────

const features = [
  { icon: "◆", label: "Full-Grain Leather" },
  { icon: "◇", label: "Handstitched" },
  { icon: "◈", label: "150+ Yrs Craft" },
  { icon: "✦", label: "Ethically Sourced" },
];

const Scene3: React.FC = () => {
  const frame = useCurrentFrame();

  const titleIn = easeOut(frame, 10, 45);

  return (
    <AbsoluteFill
      style={{
        background: `linear-gradient(160deg, #110905 0%, ${DARK} 100%)`,
        overflow: "hidden",
      }}
    >
      {/* Background diagonal lines */}
      <AbsoluteFill
        style={{
          background: `repeating-linear-gradient(
            -60deg,
            transparent,
            transparent 40px,
            rgba(201,168,76,0.018) 40px,
            rgba(201,168,76,0.018) 41px
          )`,
        }}
      />

      <Particles />

      <AbsoluteFill
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          padding: "0 80px",
          gap: 40,
        }}
      >
        {/* Header */}
        <div
          style={{
            opacity: titleIn,
            transform: `translateY(${interpolate(frame, [10, 45], [30, 0], {
              extrapolateLeft: "clamp",
              extrapolateRight: "clamp",
              easing: Easing.bezier(0.16, 1, 0.3, 1),
            })}px)`,
            textAlign: "center",
          }}
        >
          <div
            style={{
              fontFamily: "'Helvetica Neue', Arial, sans-serif",
              fontSize: 16,
              color: GOLD,
              letterSpacing: 6,
              textTransform: "uppercase",
              marginBottom: 12,
            }}
          >
            Why Kordovan
          </div>
          <div
            style={{
              fontFamily: "Georgia, serif",
              fontSize: 54,
              fontWeight: 700,
              color: CREAM,
              lineHeight: 1.15,
            }}
          >
            The Difference
            <br />
            is in the Details
          </div>
          <div
            style={{
              width: 60,
              height: 2,
              background: GOLD,
              margin: "20px auto 0",
            }}
          />
        </div>

        {/* Feature cards */}
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            gap: 20,
            width: "100%",
          }}
        >
          {features.map((f, i) => {
            const cardIn = easeOut(frame, 35 + i * 18, 65 + i * 18);
            const cardX = interpolate(
              frame,
              [35 + i * 18, 65 + i * 18],
              [-60, 0],
              {
                extrapolateLeft: "clamp",
                extrapolateRight: "clamp",
                easing: Easing.bezier(0.16, 1, 0.3, 1),
              }
            );
            return (
              <div
                key={f.label}
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 24,
                  padding: "24px 32px",
                  borderRadius: 12,
                  background: `linear-gradient(90deg, rgba(201,168,76,0.08), rgba(201,168,76,0.02))`,
                  border: `1px solid ${GOLD}22`,
                  opacity: cardIn,
                  transform: `translateX(${cardX}px)`,
                }}
              >
                <div
                  style={{
                    fontSize: 28,
                    color: GOLD,
                    width: 48,
                    textAlign: "center",
                    flexShrink: 0,
                  }}
                >
                  {f.icon}
                </div>
                <div
                  style={{
                    fontFamily: "'Helvetica Neue', Arial, sans-serif",
                    fontSize: 26,
                    color: CREAM,
                    letterSpacing: 0.5,
                    fontWeight: 500,
                  }}
                >
                  {f.label}
                </div>
              </div>
            );
          })}
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// ─── Scene 4 — CTA (360–450f = 12–15s) ───────────────────────────────────────

const Scene4: React.FC = () => {
  const frame = useCurrentFrame();

  const bgIn = easeOut(frame, 0, 30);
  const contentIn = easeOut(frame, 20, 55);
  const ctaIn = easeOut(frame, 45, 75);

  // Pulsing border on CTA button
  const pulse = interpolate(
    Math.sin((frame / 30) * Math.PI * 2),
    [-1, 1],
    [0.6, 1],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  const lineWidth = interpolate(frame, [30, 60], [0, 220], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(ellipse at 60% 50%, ${BROWN} 0%, ${DARK} 65%)`,
        opacity: bgIn,
        overflow: "hidden",
      }}
    >
      {/* Corner gold accents */}
      {[
        { top: 60, left: 60, deg: 0 },
        { top: 60, right: 60, deg: 90 },
        { bottom: 60, right: 60, deg: 180 },
        { bottom: 60, left: 60, deg: 270 },
      ].map(({ deg, ...pos }, i) => (
        <div
          key={i}
          style={{
            position: "absolute",
            ...pos,
            width: 40,
            height: 40,
            borderTop: `2px solid ${GOLD}`,
            borderLeft: `2px solid ${GOLD}`,
            transform: `rotate(${deg}deg)`,
            opacity: easeOut(frame, 15 + i * 8, 40 + i * 8),
          }}
        />
      ))}

      <Particles />

      <AbsoluteFill
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          padding: "0 80px",
          textAlign: "center",
          gap: 0,
        }}
      >
        {/* Eyebrow */}
        <div
          style={{
            opacity: contentIn,
            transform: `translateY(${interpolate(frame, [20, 55], [20, 0], {
              extrapolateLeft: "clamp",
              extrapolateRight: "clamp",
              easing: Easing.bezier(0.16, 1, 0.3, 1),
            })}px)`,
          }}
        >
          <div
            style={{
              fontFamily: "'Helvetica Neue', Arial, sans-serif",
              fontSize: 16,
              color: GOLD,
              letterSpacing: 6,
              textTransform: "uppercase",
              marginBottom: 20,
            }}
          >
            Own the Timeless
          </div>
        </div>

        {/* Main heading */}
        <div
          style={{
            opacity: contentIn,
            transform: `translateY(${interpolate(frame, [20, 55], [30, 0], {
              extrapolateLeft: "clamp",
              extrapolateRight: "clamp",
              easing: Easing.bezier(0.16, 1, 0.3, 1),
            })}px)`,
          }}
        >
          <div
            style={{
              fontFamily: "Georgia, 'Times New Roman', serif",
              fontSize: 72,
              fontWeight: 700,
              color: CREAM,
              lineHeight: 1.05,
              marginBottom: 0,
            }}
          >
            Genuine.
            <br />
            <span style={{ color: GOLD }}>Handcrafted.</span>
            <br />
            Forever.
          </div>
        </div>

        {/* Gold line */}
        <div
          style={{
            height: 2,
            width: lineWidth,
            background: `linear-gradient(90deg, transparent, ${GOLD}, transparent)`,
            margin: "32px 0",
          }}
        />

        {/* CTA Button */}
        <div
          style={{
            opacity: ctaIn,
            transform: `translateY(${interpolate(frame, [45, 75], [30, 0], {
              extrapolateLeft: "clamp",
              extrapolateRight: "clamp",
              easing: Easing.bezier(0.16, 1, 0.3, 1),
            })}px)`,
          }}
        >
          <div
            style={{
              padding: "28px 80px",
              background: GOLD,
              borderRadius: 6,
              fontFamily: "'Helvetica Neue', Arial, sans-serif",
              fontSize: 26,
              fontWeight: 700,
              color: DARK,
              letterSpacing: 3,
              textTransform: "uppercase",
              boxShadow: `0 0 40px rgba(201,168,76,${pulse * 0.4})`,
              marginBottom: 32,
            }}
          >
            Shop Now
          </div>
        </div>

        {/* URL */}
        <div
          style={{
            opacity: ctaIn,
          }}
        >
          <div
            style={{
              fontFamily: "'Helvetica Neue', Arial, sans-serif",
              fontSize: 20,
              color: `${CREAM}77`,
              letterSpacing: 2,
            }}
          >
            kordovanleather.com
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// ─── Transition wipe ─────────────────────────────────────────────────────────

const Wipe: React.FC<{ frame: number; totalFrames?: number }> = ({
  frame,
  totalFrames = 18,
}) => {
  const progress = interpolate(frame, [0, totalFrames], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.76, 0, 0.24, 1),
  });

  return (
    <AbsoluteFill
      style={{
        clipPath: `inset(0 ${(1 - progress) * 100}% 0 0)`,
        background: `${GOLD}`,
        pointerEvents: "none",
      }}
    />
  );
};

// ─── Wipe wrapper (needs own frame context inside Sequence) ──────────────────

const WipeScene: React.FC<{ totalFrames: number }> = ({ totalFrames }) => {
  const frame = useCurrentFrame();
  return <Wipe frame={frame} totalFrames={totalFrames} />;
};

// ─── Main composition ────────────────────────────────────────────────────────

export const KordovanAd: React.FC = () => {
  // Scene timing (frames)
  const wipe1Dur = 18;
  const wipe2Dur = 18;
  const wipe3Dur = 18;

  return (
    <AbsoluteFill style={{ background: DARK }}>
      {/* Scene 1: Brand reveal 0–130f */}
      <Sequence from={0} durationInFrames={148}>
        <Scene1 />
      </Sequence>

      {/* Wipe 1 */}
      <Sequence from={118} durationInFrames={wipe1Dur}>
        <WipeScene totalFrames={wipe1Dur} />
      </Sequence>

      {/* Scene 2: Product focus 128–268f */}
      <Sequence from={128} durationInFrames={140}>
        <Scene2 />
      </Sequence>

      {/* Wipe 2 */}
      <Sequence from={250} durationInFrames={wipe2Dur}>
        <WipeScene totalFrames={wipe2Dur} />
      </Sequence>

      {/* Scene 3: Feature pills 258–368f */}
      <Sequence from={258} durationInFrames={110}>
        <Scene3 />
      </Sequence>

      {/* Wipe 3 */}
      <Sequence from={350} durationInFrames={wipe3Dur}>
        <WipeScene totalFrames={wipe3Dur} />
      </Sequence>

      {/* Scene 4: CTA 358–450f */}
      <Sequence from={358} durationInFrames={92}>
        <Scene4 />
      </Sequence>
    </AbsoluteFill>
  );
};
