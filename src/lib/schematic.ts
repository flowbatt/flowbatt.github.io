export const playbackTiming = { duration: 2850, firstHold: 240, lastHold: 230 };

export function frameStart(index: number, count: number): number {
  if (index === 0) return 0;
  const hold = (playbackTiming.duration - playbackTiming.firstHold - playbackTiming.lastHold) / (count - 2);
  return playbackTiming.firstHold + (index - 1) * hold;
}

export function frameAt(elapsed: number, count: number): number {
  const position = ((elapsed % playbackTiming.duration) + playbackTiming.duration) % playbackTiming.duration;
  if (position < playbackTiming.firstHold) return 0;
  if (position >= playbackTiming.duration - playbackTiming.lastHold) return count - 1;
  const hold = (playbackTiming.duration - playbackTiming.firstHold - playbackTiming.lastHold) / (count - 2);
  return 1 + Math.floor((position - playbackTiming.firstHold) / hold);
}

export function curvePath(values: number[], cycles: number[], box: number[], xMax: number, limits: number[]): string {
  const [x, y, width, height] = box;
  // SVG clips out-of-window values; never clamp or rescale the recorded data.
  return values.map((value, i) => `${i ? 'L' : 'M'}${(x + cycles[i] / xMax * width).toFixed(4)},${(y + height - (value - limits[0]) / (limits[1] - limits[0]) * height).toFixed(4)}`).join(' ');
}
