# -*- coding: UTF-8 -*-

import json
from pkg_resources import get_distribution

from backports import tempfile
import click
from halo import Halo
from mozdownload import FactoryScraper
import mozinstall
import mozlog
from mozprofile import FirefoxProfile
from mozrunner import FirefoxRunner
import mozversion

mozlog.commandline.setup_logging("mozversion", None, {})


@click.command()
@click.option("--addon", "-a", "addons", multiple=True, help="Path to Firefox add-on")
@click.option("--preferences", "preferences", help="Path to JSON with preferences")
@click.version_option(get_distribution("fxbootstrap").version)
def cli(addons, preferences):
    with tempfile.TemporaryDirectory() as tmpdir:
        build = download(dest=tmpdir)
        binary = install(src=build, dest=tmpdir)
        profile = generate_profile(addons=addons, preferences=preferences)
        launch(binary=binary, profile=profile)


def download(dest):
    scraper = FactoryScraper("daily", destination=dest)
    spinner = Halo(text="Downloading Firefox", spinner="dots")
    spinner.start()
    path = scraper.download()
    spinner.succeed("Downloaded Firefox to {}".format(path))
    return path


def install(src, dest):
    spinner = Halo(text="Installing Firefox", spinner="dots")
    spinner.start()
    path = mozinstall.install(src=src, dest=dest)
    spinner.succeed("Installed Firefox in {}".format(path))
    return mozinstall.get_binary(path, "firefox")


def generate_profile(addons=None, preferences=None):
    if preferences is not None:
        with open(preferences) as f:
            preferences = json.load(f)
    spinner = Halo(text="Generating profile", spinner="dots")
    spinner.start()
    profile = FirefoxProfile(addons=addons, preferences=preferences)
    spinner.succeed("Generated profile at {}".format(profile.profile))
    return profile


def launch(binary, profile):
    version = mozversion.get_version(binary)
    click.echo(
        "🦊 Running {application_display_name} "
        "{application_version} "
        "({application_buildid})".format(**version)
    )
    runner = FirefoxRunner(binary=binary, profile=profile)
    runner.start()
    runner.wait()


if __name__ == "__main__":
    cli()
