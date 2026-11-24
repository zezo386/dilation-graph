import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np

fig, ax = plt.subplots(figsize=(7,7))

ax.set_title("Dilation graph")

ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.grid(True, alpha=0.2)
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_aspect('equal')

points = []
polygon_points = ax.scatter([], [], color="#3b82f6", s=50, picker=True)
polygon_edges, = ax.plot([], [], 'o-', color="#3b82f6", markersize=8, linewidth=2, picker=True)
fill_patch = None

dilation_center = (0,0)
dilation_factor = 1
dilation_marker, = ax.plot([0],[0], marker="o", color="black", zorder=5)

def draw():
    global fill_patch
    dilation_marker.set_data([dilation_center[0]], [dilation_center[1]])
    if points:
        polygon_points.set_offsets(points)

    if len(points) >= 2:
        xs = [round(p[0], 1) for p in points]
        ys = [round(p[1], 1) for p in points]

        if len(points) > 2:
            xs.append(points[0][0])
            ys.append(points[0][1])
        polygon_edges.set_data(xs, ys)
    else:
        polygon_edges.set_data([], [])
    
    if fill_patch:
        fill_patch.remove()
        fill_patch = None
    if len(points) >= 3:
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        fill_patch = ax.fill(xs, ys, color="#3b82f6", alpha=0.15, edgecolor='none', zorder=3)[0]
    
    

    fig.canvas.draw_idle()


dragging = None

def find_closest_point(x, y, min_distance=0.5):
    best_distance = min_distance
    best_idx = None
    for point in points:
        if ((point[0] - x) ** 2 + (point[1] - y) ** 2) ** 0.5 < best_distance:
            best_distance = ((point[0] - x) ** 2 + (point[1] - y) ** 2) ** 0.5
            best_idx = points.index(point)
    if ((dilation_center[0] - x) ** 2 + (dilation_center[1] - y) ** 2) ** 0.5 < best_distance:
        return -1
    return best_idx


def on_click(event):
    global dragging

    if event.inaxes != ax:
        return
    if event.button == 3:
        idx = find_closest_point(event.xdata, event.ydata)
        if idx is not None and idx != -1:
            points.pop(idx)
            draw()
        else:
            points.append((event.xdata, event.ydata))
            draw()
    
    if event.button == 1:
        idx = find_closest_point(event.xdata, event.ydata)
        if idx is not None:
            dragging = idx
    return

def on_move(event):
    global dragging
    global dilation_center
    if event.inaxes != ax or dragging is None:
        return
    if dragging == -1:
        dilation_center = (event.xdata, event.ydata)
        draw()
        return
    points[dragging] = (event.xdata, event.ydata)
    draw()
    
def on_release(event):
    global dragging
    dragging = None

fig.canvas.mpl_connect('button_press_event', on_click)
fig.canvas.mpl_connect('motion_notify_event', on_move)
fig.canvas.mpl_connect('button_release_event', on_release)

reset_ax = fig.add_axes([0.85, 0.03, 0.10, 0.05])
reset_btn = Button(reset_ax, 'Reset', color='#fee2e2', hovercolor='#fecaca')

dilation_ax = fig.add_axes([0.25,0.03, 0.5, 0.05])
dilation_slider = Slider(dilation_ax, "dilation factor", 0, 10, valinit=1,valstep=0.1)

def on_reset(_):
    global dilation_center
    points.clear()
    polygon_edges.set_data([], [])
    polygon_points.set_offsets(np.empty((0,2)))
    dilation_center = (0,0)
    draw()
reset_btn.on_clicked(on_reset)

def on_slider_change(value):
    global dilation_factor
    dilation_factor = value
dilation_slider.on_changed(on_slider_change)



plt.show()



