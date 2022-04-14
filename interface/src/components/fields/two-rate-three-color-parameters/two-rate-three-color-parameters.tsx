import React, { ReactElement, useEffect, useMemo } from 'react';
import { StateUpdater } from '@/commons/change-handler';
import { useNfvTeFunctionParameters } from '@/commons/nfv-te-values';
import { TwoRateThreeColorIntervalField } from './two-rate-three-color-interval-field';
import { TwoRateThreeColorBucketFSizeField } from './two-rate-three-color-bucket-f-size-field';
import { TwoRateThreeColorBucketFMaxSizeField } from './two-rate-three-color-bucket-f-max-size-field';
import { TwoRateThreeColorBucketSSizeField } from './two-rate-three-color-bucket-s-size-field';
import { TwoRateThreeColorBucketSMaxSizeField } from './two-rate-three-color-bucket-s-max-size-field';
import { TwoRateThreeColorRateFField } from './two-rate-three-color-rate-f-field';
import { TwoRateThreeColorColorAwareField } from './two-rate-three-color-color-aware-field';
import { TwoRateThreeColorCaBucketFSizeField } from './two-rate-three-color-ca-bucket-f-size-field';
import { TwoRateThreeColorCaBucketFMaxSizeField } from './two-rate-three-color-ca-bucket-f-max-size-field';
import { TwoRateThreeColorCaBucketSSizeField } from './two-rate-three-color-ca-bucket-s-size-field';
import { TwoRateThreeColorCaBucketSMaxSizeField } from './two-rate-three-color-ca-bucket-s-max-size-field';
import { TwoRateThreeColorCaRateSField } from './two-rate-three-color-ca-rate-s-field';
import { TwoRateThreeColorRateSField } from './two-rate-three-color-rate-s-field';
import { TwoRateThreeColorCaRateFField } from './two-rate-three-color-ca-rate-f-field';

type TwoRateThreeColorParameters = {
  rateF: string,
  rateS: string,
  bucketF_size: string,
  bucketF_max_size: string,
  bucketS_size: string,
  bucketS_max_size: string,
  interval: string,
  color_aware?: string,
  ca_bucketF_size?: string,
  ca_bucketF_max_size?: string,
  ca_bucketS_size?: string,
  ca_bucketS_max_size?: string,
  ca_rateF?: string,
  ca_rateS?: string,
};

export function TwoRateThreeColorParameters(): ReactElement {
  const [
    twoRateThreeColorParameters,
    setTwoRateThreeColorParameters,
  ] = useNfvTeFunctionParameters<TwoRateThreeColorParameters>();

  useSetTwoRateThreeColorInitialParameters(setTwoRateThreeColorParameters);

  const isColorAwareEnabled = useMemo(() => {
    return twoRateThreeColorParameters.color_aware;
  }, [twoRateThreeColorParameters]);

  useDeleteColorAwareParametersWhenDisabled(isColorAwareEnabled, setTwoRateThreeColorParameters);

  return (
    <>
      <TwoRateThreeColorBucketFSizeField
        twoRateThreeColorParameters={twoRateThreeColorParameters}
        setTwoRateThreeColorParameters={setTwoRateThreeColorParameters}
      />

      <TwoRateThreeColorBucketFMaxSizeField
        twoRateThreeColorParameters={twoRateThreeColorParameters}
        setTwoRateThreeColorParameters={setTwoRateThreeColorParameters}
      />

      <TwoRateThreeColorRateFField
        twoRateThreeColorParameters={twoRateThreeColorParameters}
        setTwoRateThreeColorParameters={setTwoRateThreeColorParameters}
      />

      <TwoRateThreeColorBucketSSizeField
        twoRateThreeColorParameters={twoRateThreeColorParameters}
        setTwoRateThreeColorParameters={setTwoRateThreeColorParameters}
      />

      <TwoRateThreeColorBucketSMaxSizeField
        twoRateThreeColorParameters={twoRateThreeColorParameters}
        setTwoRateThreeColorParameters={setTwoRateThreeColorParameters}
      />

      <TwoRateThreeColorRateSField
        twoRateThreeColorParameters={twoRateThreeColorParameters}
        setTwoRateThreeColorParameters={setTwoRateThreeColorParameters}
      />

      <TwoRateThreeColorIntervalField
        twoRateThreeColorParameters={twoRateThreeColorParameters}
        setTwoRateThreeColorParameters={setTwoRateThreeColorParameters}
      />

      <TwoRateThreeColorColorAwareField
        twoRateThreeColorParameters={twoRateThreeColorParameters}
        setTwoRateThreeColorParameters={setTwoRateThreeColorParameters}
      />

      {isColorAwareEnabled && <>
        <TwoRateThreeColorCaBucketFSizeField
          twoRateThreeColorParameters={twoRateThreeColorParameters}
          setTwoRateThreeColorParameters={setTwoRateThreeColorParameters}
        />

        <TwoRateThreeColorCaBucketFMaxSizeField
          twoRateThreeColorParameters={twoRateThreeColorParameters}
          setTwoRateThreeColorParameters={setTwoRateThreeColorParameters}
        />

        <TwoRateThreeColorCaRateFField
          twoRateThreeColorParameters={twoRateThreeColorParameters}
          setTwoRateThreeColorParameters={setTwoRateThreeColorParameters}
        />

        <TwoRateThreeColorCaBucketSSizeField
          twoRateThreeColorParameters={twoRateThreeColorParameters}
          setTwoRateThreeColorParameters={setTwoRateThreeColorParameters}
        />

        <TwoRateThreeColorCaBucketSMaxSizeField
          twoRateThreeColorParameters={twoRateThreeColorParameters}
          setTwoRateThreeColorParameters={setTwoRateThreeColorParameters}
        />

        <TwoRateThreeColorCaRateSField
          twoRateThreeColorParameters={twoRateThreeColorParameters}
          setTwoRateThreeColorParameters={setTwoRateThreeColorParameters}
        />
      </>}
    </>
  );
}

export interface TwoRateThreeColorParameterFieldProps {
  twoRateThreeColorParameters: TwoRateThreeColorParameters,
  setTwoRateThreeColorParameters: StateUpdater<TwoRateThreeColorParameters>,
}

function useSetTwoRateThreeColorInitialParameters(
  setTwoRateThreeColorParameters: StateUpdater<TwoRateThreeColorParameters>,
): void {
  useEffect(() => {
    setTwoRateThreeColorParameters({
      rateF: '',
      rateS: '',
      bucketF_size: '',
      bucketF_max_size: '',
      bucketS_size: '',
      bucketS_max_size: '',
      interval: '',
    });
  }, [setTwoRateThreeColorParameters]);
}

function useDeleteColorAwareParametersWhenDisabled(
  isColorAwareEnabled: TwoRateThreeColorParameters['color_aware'],
  setTwoRateThreeColorParameters: StateUpdater<TwoRateThreeColorParameters>,
): void {
  useEffect(() => {
    if(!isColorAwareEnabled) {
      setTwoRateThreeColorParameters(currentParameters => {
        delete currentParameters.ca_bucketF_size;
        delete currentParameters.ca_bucketF_max_size;
        delete currentParameters.ca_bucketS_size;
        delete currentParameters.ca_bucketS_max_size;
        delete currentParameters.ca_rateS;
        delete currentParameters.ca_rateF;
        return currentParameters;
      });
    }
  }, [isColorAwareEnabled, setTwoRateThreeColorParameters]);
}
