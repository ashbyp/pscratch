import hydra
from omegaconf import DictConfig


@hydra.main(version_base=None, config_path="conf", config_name="config")
def main(cfg: DictConfig) -> None:
    print(cfg)
    print(cfg['params']['c'])
    print(cfg['env']['db'])


if __name__ == '__main__':
    main()
