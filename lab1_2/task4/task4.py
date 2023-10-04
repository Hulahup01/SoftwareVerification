"""
Task 4. Write a program that generates an HTML file with a table in which the background of the lines gradually
changes from white to black (with the minimum possible step). See the example in the picture. All
parameters of the table, its contents, etc. are at your discretion. The main thing is to make it as
similar as possible to the picture.
"""


def task4_solv():
    with open('gradient.html', 'w') as f:
        f.write("""<!DOCTYPE html>
    <html>
    <head>
    <title>GRADIENT</title>
        <style>
            table {
                width: 100%; 
                height: 100%;
                border-collapse: collapse;
            }

            td {    
                height: 0.19vh;
            }
        </style>
    </head>
    <body style="padding: 0; margin: 0; overflow: hidden;">
        <table>
    """)

        num_rows = 256

        # Generate the rows with particular background
        for i in range(num_rows):
            gradient_color = "rgb({}, {}, {})".format(
                int(255 - i * (255 / (num_rows - 1))),
                int(255 - i * (255 / (num_rows - 1))),
                int(255 - i * (255 / (num_rows - 1)))
            )

            f.write('<tr style="background-color: {};">'.format(gradient_color))
            f.write('<td></td>')
            f.write('</tr>\n')

        f.write('</table>\n</body>\n</html>')

    print("Done")


if __name__ == "__main__":
    task4_solv()
