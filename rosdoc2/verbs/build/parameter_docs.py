import os
import yaml

parameter_mainpage_rst = """\
Parameters
==========

.. toctree::
   :maxdepth: 1

{parameters_toc}
"""


def generate_parameter_docs(
    package_xml_directory, parameter_files, wrapped_sphinx_directory
):
    """."""
    print("Generating parameter docs for", parameter_files)
    toc = ""

    for param_file in parameter_files:
        print("generating", param_file)
        param_file_path = os.path.join(package_xml_directory, param_file)
        with open(param_file_path) as f:
            yaml_data: map = yaml.safe_load(f)
            # Get first key
            node_name = next(iter(yaml_data))
            print("node name", node_name)
        print(
            "writing to", os.path.join(wrapped_sphinx_directory, f"__{node_name}.rst")
        )
        with open(
            os.path.join(wrapped_sphinx_directory, f"__{node_name}.rst"), "w"
        ) as f:
            file_contents = f"{node_name}\n"
            file_contents += "=" * len(node_name) + "\n\n"
            file_contents += f".. generate_parameter_library_details:: {param_file_path}"
            f.write(file_contents)
        toc += f"   __{node_name}\n"

    param_content = parameter_mainpage_rst.format_map({"parameters_toc": toc})
    param_rst_path = os.path.join(wrapped_sphinx_directory, "__parameters.rst")
    with open(param_rst_path, "w") as f:
        f.write(param_content)
