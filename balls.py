import pygame
import math
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Spinning Hexagon with Ball")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Hexagon parameters
hex_radius = 200
center = (screen_width // 2, screen_height // 2)
rotation_speed = 1  # radians per second

# Ball parameters
ball_radius = 10
ball_color = RED
gravity = 300  # pixels per second squared
restitution = 0.8  # energy retained after collision

# Initial ball state
ball_x, ball_y = center
ball_vx, ball_vy = 0, 0

# Precompute local vertices and edges for hexagon
local_vertices = []
for i in range(6):
    angle_deg = 60 * i
    angle_rad = math.radians(angle_deg)
    x = hex_radius * math.cos(angle_rad)
    y = hex_radius * math.sin(angle_rad)
    local_vertices.append((x, y))

edges = []
for i in range(6):
    v1 = local_vertices[i]
    v2 = local_vertices[(i + 1) % 6]
    
    # Edge line equation: a*x + b*y + c = 0
    a = v2[1] - v1[1]
    b = v1[0] - v2[0]
    c = v2[0] * v1[1] - v1[0] * v2[1]
    
    # Compute inward-pointing normal
    edge_vec = (v2[0] - v1[0], v2[1] - v1[1])
    normal = (-edge_vec[1], edge_vec[0])  # Rotate edge vector 90 degrees counter-clockwise
    length = math.hypot(normal[0], normal[1])
    if length == 0:
        normal = (0, 0)
    else:
        normal = (normal[0] / length, normal[1] / length)
    
    edges.append({'a': a, 'b': b, 'c': c, 'normal': normal})

# Rotation angle
theta = 0

# Clock for controlling frame rate
clock = pygame.time.Clock()
running = True

while running:
    # Delta time in seconds
    dt = clock.tick(60) / 1000.0
    
    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    # Update hexagon rotation
    theta += rotation_speed * dt
    
    # Apply gravity to ball
    ball_vy += gravity * dt
    
    # Update ball position
    ball_x += ball_vx * dt
    ball_y += ball_vy * dt
    
    # Check collision with hexagon
    # Translate ball to hexagon's local coordinates
    local_x = ball_x - center[0]
    local_y = ball_y - center[1]
    
    # Rotate by -theta
    cos_theta = math.cos(-theta)
    sin_theta = math.sin(-theta)
    rotated_x = local_x * cos_theta - local_y * sin_theta
    rotated_y = local_x * sin_theta + local_y * cos_theta
    
    # Check if the rotated point is inside the hexagon
    is_inside = True
    for edge in edges:
        a = edge['a']
        b = edge['b']
        c = edge['c']
        val = a * rotated_x + b * rotated_y + c
        if val * c < 0:
            is_inside = False
            break
    
    if not is_inside:
        # Find the closest edge
        min_distance = float('inf')
        closest_edge = None
        point = (rotated_x, rotated_y)
        
        for edge in edges:
            a = edge['a']
            b = edge['b']
            c = edge['c']
            distance = abs(a * point[0] + b * point[1] + c) / math.hypot(a, b)
            if distance < min_distance:
                min_distance = distance
                closest_edge = edge
        
        # Get normal in local frame and rotate to global frame
        normal_local = closest_edge['normal']
        cos_theta_rot = math.cos(theta)
        sin_theta_rot = math.sin(theta)
        normal_global = (
            normal_local[0] * cos_theta_rot - normal_local[1] * sin_theta_rot,
            normal_local[0] * sin_theta_rot + normal_local[1] * cos_theta_rot
        )
        
        # Reflect velocity
        dot_product = ball_vx * normal_global[0] + ball_vy * normal_global[1]
        ball_vx -= 2 * dot_product * normal_global[0] * restitution
        ball_vy -= 2 * dot_product * normal_global[1] * restitution
        
        # Adjust position to prevent sticking
        ball_x += normal_global[0] * min_distance
        ball_y += normal_global[1] * min_distance
    
    # Draw everything
    screen.fill(WHITE)
    
    # Draw hexagon
    current_vertices = []
    for (x, y) in local_vertices:
        x_rot = x * math.cos(theta) - y * math.sin(theta)
        y_rot = x * math.sin(theta) + y * math.cos(theta)
        current_vertices.append((x_rot + center[0], y_rot + center[1]))
    pygame.draw.polygon(screen, BLACK, current_vertices, 2)
    
    # Draw ball
    pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)
    
    pygame.display.flip()

pygame.quit()